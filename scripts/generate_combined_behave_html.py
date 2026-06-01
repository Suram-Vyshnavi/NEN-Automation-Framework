import datetime
import glob
import html
import json
import os
import sys
from pathlib import Path


def scenario_status(steps):
    statuses = [((step.get("result") or {}).get("status") or "").lower() for step in steps]
    if any(status == "failed" for status in statuses):
        return "failed"
    if any(status in {"undefined", "untested", "skipped"} for status in statuses):
        return "skipped"
    return "passed"


def load_scenarios(json_files):
    rows = []
    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (json.JSONDecodeError, ValueError, OSError):
            print(f"Skipping invalid/empty JSON: {file_path}")
            continue
        if not isinstance(data, list):
            continue

        for feature in data:
            feature_name = feature.get("name", "Unknown Feature")
            for scenario in feature.get("elements", []):
                if scenario.get("type") not in {"scenario", "background"}:
                    continue
                row = {
                    "feature": feature_name,
                    "scenario": scenario.get("name", "Unknown Scenario"),
                    "status": scenario_status(scenario.get("steps", [])),
                }
                rows.append(row)
    return rows


def render_html(rows, output_file):
    total = len(rows)
    passed = sum(1 for row in rows if row["status"] == "passed")
    failed = sum(1 for row in rows if row["status"] == "failed")
    skipped = sum(1 for row in rows if row["status"] == "skipped")
    generated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status_class = {
        "passed": "ok",
        "failed": "bad",
        "skipped": "warn",
    }

    rows_html = "\n".join(
        [
            "<tr>"
            f"<td>{html.escape(row['feature'])}</td>"
            f"<td>{html.escape(row['scenario'])}</td>"
            f"<td><span class='pill {status_class.get(row['status'], 'warn')}'>{html.escape(row['status'].upper())}</span></td>"
            "</tr>"
            for row in rows
        ]
    )

    page = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
  <title>NEN Combined Behave Report</title>
  <style>
    body {{
      margin: 0;
      font-family: Segoe UI, Tahoma, Arial, sans-serif;
      background: #f5f7fb;
      color: #1a1f36;
    }}
    .wrap {{
      max-width: 1200px;
      margin: 24px auto;
      padding: 0 16px 24px;
    }}
    .card {{
      background: #fff;
      border: 1px solid #dfe4ee;
      border-radius: 10px;
      box-shadow: 0 4px 18px rgba(9, 30, 66, 0.06);
    }}
    .header {{
      padding: 16px 20px;
      border-bottom: 1px solid #e8edf5;
    }}
    .title {{
      margin: 0;
      font-size: 20px;
      font-weight: 700;
    }}
    .meta {{
      margin-top: 6px;
      font-size: 13px;
      color: #55607a;
    }}
    .summary {{
      display: grid;
      grid-template-columns: repeat(4, minmax(120px, 1fr));
      gap: 12px;
      padding: 16px 20px;
    }}
    .kpi {{
      border: 1px solid #e3e8f2;
      border-radius: 8px;
      padding: 10px 12px;
      background: #fbfcff;
    }}
    .kpi .label {{ font-size: 12px; color: #5a6785; }}
    .kpi .val {{ font-size: 22px; font-weight: 700; margin-top: 4px; }}
    .table-wrap {{
      overflow: auto;
      padding: 0 20px 20px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 780px;
      background: #fff;
    }}
    th, td {{
      text-align: left;
      padding: 10px 12px;
      border-bottom: 1px solid #eef2f8;
      font-size: 14px;
    }}
    th {{
      position: sticky;
      top: 0;
      background: #f8faff;
      z-index: 1;
      font-weight: 600;
      color: #2c3650;
    }}
    .pill {{
      display: inline-block;
      min-width: 74px;
      text-align: center;
      border-radius: 999px;
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.2px;
      color: #fff;
    }}
    .ok {{ background: #0f8a2d; }}
    .bad {{ background: #c62828; }}
    .warn {{ background: #a66a00; }}
    @media (max-width: 720px) {{
      .summary {{ grid-template-columns: repeat(2, minmax(120px, 1fr)); }}
    }}
  </style>
</head>
<body>
  <div class=\"wrap\">
    <div class=\"card\">
      <div class=\"header\">
        <h1 class=\"title\">NEN Combined Behave Report</h1>
        <div class=\"meta\">Generated at: {generated_at}</div>
      </div>

      <div class=\"summary\">
        <div class=\"kpi\"><div class=\"label\">Total Scenarios</div><div class=\"val\">{total}</div></div>
        <div class=\"kpi\"><div class=\"label\">Passed</div><div class=\"val\">{passed}</div></div>
        <div class=\"kpi\"><div class=\"label\">Failed</div><div class=\"val\">{failed}</div></div>
        <div class=\"kpi\"><div class=\"label\">Skipped</div><div class=\"val\">{skipped}</div></div>
      </div>

      <div class=\"table-wrap\">
        <table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Scenario</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {rows_html}
          </tbody>
        </table>
      </div>
    </div>
  </div>
</body>
</html>
"""

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(page, encoding="utf-8")


def main():
    input_glob = sys.argv[1] if len(sys.argv) > 1 else "reports/json-report/*.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "reports/html-report/report.html"

    json_files = sorted(glob.glob(input_glob))
    if not json_files:
        print(f"No JSON files found with pattern: {input_glob}")
        return 1

    rows = load_scenarios(json_files)
    render_html(rows, output_file)
    print(f"Combined HTML report created: {output_file}")
    print(f"Scenarios included: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
