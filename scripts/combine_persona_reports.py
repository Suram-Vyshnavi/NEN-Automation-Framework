"""
Combine individual per-persona behave_html_formatter HTML reports into one
tabbed HTML file.  Each persona gets its own tab; the tab content is the
*full body* of the original report (CSS + JS + screenshots included inline).
"""
import os
import sys
import re
import datetime
from pathlib import Path

PERSONA_ORDER = [
    "student",
    "faculty",
    "mentor",
    "rm",
    "incubator",
    "viability",
    "cohort_manager",
    "evaluator",
]

PERSONA_LABELS = {
    "student":        "Student",
    "faculty":        "Faculty",
    "mentor":         "Mentor",
    "rm":             "Regional Manager",
    "incubator":      "Incubator",
    "viability":      "Viability Specialist",
    "cohort_manager": "Cohort Manager",
    "evaluator":      "Evaluator",
}


def _extract_body_and_head(html_text: str):
    """Return (head_extras, body_html) from a behave HTML report."""
    # Extract everything inside <style> tags from <head>
    styles = re.findall(r"<style[^>]*>(.*?)</style>", html_text, re.DOTALL | re.IGNORECASE)
    # Extract everything inside <script> tags
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html_text, re.DOTALL | re.IGNORECASE)
    # Extract <body> contents
    body_match = re.search(r"<body[^>]*>(.*?)</body>", html_text, re.DOTALL | re.IGNORECASE)
    body_html = body_match.group(1).strip() if body_match else html_text
    return styles, scripts, body_html


def _detect_status(body_html: str) -> str:
  """Detect pass/fail from behave summary totals in the report body."""
  scenario_line_match = re.search(r"Scenarios:(.*?)(?:</p>|<br|$)", body_html, re.IGNORECASE)
  if scenario_line_match:
    failed_match = re.search(r"failed:\s*(\d+)", scenario_line_match.group(1), re.IGNORECASE)
    if failed_match:
      failed_count = int(failed_match.group(1))
      return "failed" if failed_count > 0 else "passed"

  feature_line_match = re.search(r"Features:(.*?)(?:</p>|<br|$)", body_html, re.IGNORECASE)
  if feature_line_match:
    failed_match = re.search(r"failed:\s*(\d+)", feature_line_match.group(1), re.IGNORECASE)
    if failed_match:
      failed_count = int(failed_match.group(1))
      return "failed" if failed_count > 0 else "passed"

  return "failed" if "Failing scenarios" in body_html else "passed"


def _namespace_body_ids(body_html: str, prefix: str) -> str:
    """Prefix element IDs and toggle targets to avoid cross-tab collisions."""

    def _replace_id_attr(match: re.Match) -> str:
        original_id = match.group(1)
        return f'id="{prefix}__{original_id}"'

    def _replace_toggle_target(match: re.Match) -> str:
        quote = match.group(1)
        target = match.group(2)
        return f"Collapsible_toggle({quote}{prefix}__{target}{quote})"

    namespaced = re.sub(r'\bid="([^"]+)"', _replace_id_attr, body_html)
    # Behave uses this pattern for scenario rows and embedded error/screenshot blocks.
    namespaced = re.sub(
        r"Collapsible_toggle\((['\"])([^'\"]+)\1\)",
        _replace_toggle_target,
        namespaced,
    )
    return namespaced


def _remove_behave_title(body_html: str) -> str:
    """Remove the embedded Behave Test Report heading from each tab body."""
    return re.sub(
        r"<h1>\s*Behave\s+Test\s+Report\s*</h1>",
        "",
        body_html,
        flags=re.IGNORECASE,
    )


def build_combined(input_dir: str, output_file: str):
    input_path = Path(input_dir)
    html_files = {p.stem: p for p in input_path.glob("*.html")}

    if not html_files:
        print(f"No HTML files found in: {input_dir}")
        return 1

    # Sort by PERSONA_ORDER, then alphabetically for unknown names
    ordered = []
    for name in PERSONA_ORDER:
        if name in html_files:
            ordered.append((name, html_files[name]))
    for name, path in sorted(html_files.items()):
        if name not in PERSONA_ORDER:
            ordered.append((name, path))

    all_styles = set()
    all_scripts = set()
    tabs = []

    for name, path in ordered:
        try:
            html_text = path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"Skipping {path}: {e}")
            continue

        styles, scripts, body_html = _extract_body_and_head(html_text)
        for s in styles:
            all_styles.add(s.strip())
        for s in scripts:
            all_scripts.add(s.strip())

        label = PERSONA_LABELS.get(name, name.replace("_", " ").title())
        status = _detect_status(body_html)
        body_html = _remove_behave_title(body_html)
        body_html = _namespace_body_ids(body_html, name)
        tabs.append((name, label, status, body_html))

    if not tabs:
        print("No valid HTML reports could be parsed.")
        return 1

    total = len(tabs)
    passed = sum(1 for _, _, s, _ in tabs if s == "passed")
    failed = total - passed
    generated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build tab buttons
    tab_buttons_html = "\n".join(
        f'<button class="tab-btn{" active" if i == 0 else ""} status-{status}" '
        f'onclick="showTab(\'{name}\')" id="btn-{name}">'
        f'<span class="tab-icon">{"✅" if status == "passed" else "❌"}</span> {label}'
        f'</button>'
        for i, (name, label, status, _) in enumerate(tabs)
    )

    # Build tab panels
    tab_panels_html = "\n".join(
        f'<div class="tab-panel{" active" if i == 0 else ""}" id="tab-{name}">'
        f'{body_html}'
        f'</div>'
        for i, (name, _, _, body_html) in enumerate(tabs)
    )

    # Merge all collected styles/scripts
    merged_styles = "\n".join(all_styles)
    merged_scripts = "\n".join(all_scripts)

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>NEN Automation - Combined Persona Report</title>
  <style>
    /* ── Original behave_html_formatter styles ── */
    {merged_styles}

    /* ── Combined report shell styles ── */
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Segoe UI, Tahoma, Arial, sans-serif;
      background: #f0f2f7;
      color: #1a1f36;
    }}
    .shell-header {{
      background: #1a237e;
      color: #fff;
      padding: 14px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }}
    .shell-header h1 {{
      margin: 0;
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 0.3px;
    }}
    .shell-header .meta {{
      font-size: 12px;
      opacity: 0.75;
      margin-top: 3px;
    }}
    .summary-bar {{
      background: #fff;
      border-bottom: 1px solid #dde3f0;
      padding: 10px 28px;
      display: flex;
      gap: 24px;
      align-items: center;
    }}
    .kpi {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
    }}
    .kpi .val {{
      font-size: 20px;
      font-weight: 700;
    }}
    .kpi.total .val {{ color: #1a237e; }}
    .kpi.pass .val  {{ color: #1b7a37; }}
    .kpi.fail .val  {{ color: #c62828; }}
    .tab-bar {{
      background: #fff;
      border-bottom: 2px solid #d0d8ed;
      padding: 0 20px;
      display: flex;
      flex-wrap: wrap;
      gap: 2px;
      overflow-x: auto;
    }}
    .tab-btn {{
      border: none;
      background: transparent;
      padding: 11px 18px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      color: #5a6785;
      border-bottom: 3px solid transparent;
      margin-bottom: -2px;
      transition: color 0.15s, border-color 0.15s;
      white-space: nowrap;
    }}
    .tab-btn:hover {{ color: #1a237e; }}
    .tab-btn.active {{ color: #1a237e; border-bottom-color: #1a237e; }}
    .tab-btn.status-failed {{ color: #b71c1c; }}
    .tab-btn.active.status-failed {{ border-bottom-color: #c62828; }}
    .tab-icon {{ font-style: normal; }}
    .tab-panel {{ display: none; padding: 20px 20px; }}
    .tab-panel.active {{ display: block; }}
    .tab-content .behave #label h1 {{ display: none; }}
  </style>
</head>
<body>
  <div class="shell-header">
    <div>
      <h1>NEN Automation — Combined Persona Report</h1>
      <div class="meta">Generated: {generated_at}</div>
    </div>
  </div>
  <div class="summary-bar">
    <div class="kpi total"><span class="val">{total}</span> <span>Personas</span></div>
    <div class="kpi pass"><span class="val">{passed}</span> <span>Passed</span></div>
    <div class="kpi fail"><span class="val">{failed}</span> <span>Failed</span></div>
  </div>
  <div class="tab-bar">
    {tab_buttons_html}
  </div>
  <div class="tab-content">
    {tab_panels_html}
  </div>

  <script>
    {merged_scripts}

    function showTab(name) {{
      document.querySelectorAll('.tab-panel').forEach(function(p) {{
        p.classList.remove('active');
      }});
      document.querySelectorAll('.tab-btn').forEach(function(b) {{
        b.classList.remove('active');
      }});
      var panel = document.getElementById('tab-' + name);
      var btn   = document.getElementById('btn-' + name);
      if (panel) panel.classList.add('active');
      if (btn)   btn.classList.add('active');
    }}
  </script>
</body>
</html>
"""

    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page, encoding="utf-8")
    print(f"Combined persona report created: {output_file}")
    print(f"Personas included: {len(tabs)} | Passed: {passed} | Failed: {failed}")
    return 0


def main():
    input_dir   = sys.argv[1] if len(sys.argv) > 1 else "reports/html-report/personas"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "reports/html-report/combined_report.html"
    return build_combined(input_dir, output_file)


if __name__ == "__main__":
    raise SystemExit(main())
