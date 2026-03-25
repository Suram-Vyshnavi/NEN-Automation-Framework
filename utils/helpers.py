import allure
from allure_commons.types import AttachmentType

def attach_screenshot(page,name="Screenshot"):
    allure.attach(page.screenshot(full_page=True),name=name,attachment_type=AttachmentType.PNG)

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
                # Highlight all matching elements
                for i in range(count):
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
                for i in range(count):
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


