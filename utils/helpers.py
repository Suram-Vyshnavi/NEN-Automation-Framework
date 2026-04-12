import allure
import base64
from allure_commons.types import AttachmentType


_REPORT_CONTEXT = None
_FAILURE_MARKERS = ("fail", "failed", "error", "exception", "abort")


def set_report_context(context):
    """Store the active Behave context so report embedding works without passing context everywhere."""
    global _REPORT_CONTEXT
    _REPORT_CONTEXT = context

def attach_screenshot(page, name="Screenshot", context=None, force=False):
    """Attach screenshot to reports.

    By default, captures only for failure-like names to avoid success-noise.
    Pass force=True to always capture.
    """
    lowered = str(name).lower()
    if not force and not any(marker in lowered for marker in _FAILURE_MARKERS):
        return
    try:
        screenshot_bytes = page.screenshot(full_page=True)
    except Exception as exc:
        print(f"Screenshot capture failed: {exc}")
        return

    # Allure attachment
    try:
        allure.attach(screenshot_bytes, name=name, attachment_type=AttachmentType.PNG)
    except Exception:
        pass  # No active Allure context — safe to skip.

    # behave-html-formatter attachment
    active_context = context if context is not None else _REPORT_CONTEXT
    if active_context is not None:
        try:
            # Behave context API: attach(mime_type, data). For HTML formatter,
            # image payload is expected as base64 text.
            encoded_image = base64.b64encode(screenshot_bytes).decode("utf-8")
            active_context.attach("image/png", encoded_image)
        except Exception:
            pass  # behave-html-formatter not active or context doesn't support embed.

def highlight_element(page, locator, duration: int = 1500):
    """Highlight an element by adding a red border temporarily.
    
    Args:
        page: Playwright page object
        locator: Element locator (can be string or locator object)
        duration: How long to highlight in milliseconds (default 1500ms)
    """
    try:
        # Convert string locator to locator object if needed
        if isinstance(locator, str):
            element = page.locator(locator)
        else:
            element = locator
        
        # Check if locator resolves to multiple elements
        try:
            count = element.count()
            if count > 1:
                capped_count = min(count, 20)
                # Highlight all matching elements
                for i in range(capped_count):
                    single_element = element.nth(i)
                    try:
                        single_element.scroll_into_view_if_needed(timeout=1000)
                        page.evaluate("""
                            (el) => {
                                if (el) {
                                    el.style.border = '5px solid red';
                                    el.style.backgroundColor = 'rgba(255, 0, 0, 0.2)';
                                    el.style.outline = '3px solid yellow';
                                }
                            }
                        """, single_element.element_handle())
                    except:
                        pass
                
                page.wait_for_timeout(100)
                
                # Remove highlights
                for i in range(capped_count):
                    single_element = element.nth(i)
                    try:
                        page.evaluate("""
                            (el) => {
                                if (el) {
                                    el.style.border = '';
                                    el.style.backgroundColor = '';
                                    el.style.outline = '';
                                }
                            }
                        """, single_element.element_handle())
                    except:
                        pass
                return
        except:
            pass
        
        # Single element highlighting
        element.scroll_into_view_if_needed(timeout=1000)
        
        # Scroll up a bit to ensure title/heading is fully visible (not cut off at top)
        page.evaluate("window.scrollBy(0, -150)")
        
        # Add red border with JavaScript
        page.evaluate("""
            (element) => {
                if (element) {
                    element.style.border = '5px solid red';
                    element.style.backgroundColor = 'rgba(255, 0, 0, 0.2)';
                    element.style.outline = '3px solid yellow';
                }
            }
        """, element.element_handle())
        
        # Wait briefly for visualization
        page.wait_for_timeout(200)
        
        # Remove the highlight
        page.evaluate("""
            (element) => {
                if (element) {
                    element.style.border = '';
                    element.style.backgroundColor = '';
                    element.style.outline = '';
                }
            }
        """, element.element_handle())
    except Exception as e:
        print(f"Could not highlight element: {e}")


