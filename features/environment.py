from playwright.sync_api import sync_playwright
import os
import traceback
from pages.common.login_page import LoginPage
from utils.helpers import attach_screenshot, set_report_context

# Global flag to track if setup is done
setup_complete = False


def _env_to_bool(env_value, default=True):
    if env_value is None:
        return default
    return str(env_value).strip().lower() in ("1", "true", "yes", "y", "on")


def _is_ci_environment():
    # Keep CI detection strict and explicit to avoid false positives locally.
    return _env_to_bool(os.getenv("CI"), default=False) or _env_to_bool(
        os.getenv("GITHUB_ACTIONS"), default=False
    )


def _resolve_headless_mode():
    """Resolve launch mode with deterministic precedence.

    Rules:
    1) CI is always headless.
    2) Local runs follow HEADLESS env var.
    3) If HEADLESS is unset locally, default to headed.
    """
    is_ci = _is_ci_environment()
    if is_ci:
        return True, is_ci

    requested_headless = _env_to_bool(os.getenv("HEADLESS"), default=False)
    return requested_headless, is_ci


def _safe_close(resource, name):
    try:
        if resource:
            resource.close()
    except Exception as exc:
        print(f"Failed to close {name}: {exc}")


def _safe_stop(playwright_obj):
    try:
        if playwright_obj:
            playwright_obj.stop()
    except Exception as exc:
        print(f"Failed to stop Playwright: {exc}")


def _install_highlight_wrappers():
    # Ensure every click/fill interaction scrolls into view and highlights the target element
    # This wraps Playwright methods at runtime so page objects don't need to change.
    from utils.helpers import highlight_element
    from playwright.sync_api import Locator, Page

    def _assert_visible(page, locator_or_selector, step_name):
        try:
            locator = (
                page.locator(locator_or_selector)
                if isinstance(locator_or_selector, str)
                else locator_or_selector
            )
            locator.first.wait_for(state="visible", timeout=10000)
            assert locator.first.is_visible(), f"Element is not visible for {step_name}"
        except Exception as exc:
            attach_screenshot(page, f"{step_name} Visibility Assertion Failed", force=True)
            raise AssertionError(f"Visibility assertion failed for {step_name}: {exc}") from exc

    # Wrap Page.click to highlight before clicking
    _orig_page_click = Page.click

    def _highlighted_page_click(self, selector, *args, **kwargs):
        _assert_visible(self, selector, "Page.click")
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_click(self, selector, *args, **kwargs)

    Page.click = _highlighted_page_click

    # Wrap Locator.click to highlight before clicking
    _orig_locator_click = Locator.click

    def _highlighted_locator_click(self, *args, **kwargs):
        _assert_visible(self.page, self, "Locator.click")
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_click(self, *args, **kwargs)

    Locator.click = _highlighted_locator_click

    # Wrap Page.fill to highlight before filling
    _orig_page_fill = Page.fill

    def _highlighted_page_fill(self, selector, text, *args, **kwargs):
        _assert_visible(self, selector, "Page.fill")
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_fill(self, selector, text, *args, **kwargs)

    Page.fill = _highlighted_page_fill

    # Wrap Locator.fill to highlight before filling
    _orig_locator_fill = Locator.fill

    def _highlighted_locator_fill(self, text, *args, **kwargs):
        _assert_visible(self.page, self, "Locator.fill")
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_fill(self, text, *args, **kwargs)

    Locator.fill = _highlighted_locator_fill

    # Wrap Page.check/uncheck to highlight before interacting
    _orig_page_check = Page.check

    def _highlighted_page_check(self, selector, *args, **kwargs):
        _assert_visible(self, selector, "Page.check")
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_check(self, selector, *args, **kwargs)

    Page.check = _highlighted_page_check

    _orig_page_uncheck = Page.uncheck

    def _highlighted_page_uncheck(self, selector, *args, **kwargs):
        _assert_visible(self, selector, "Page.uncheck")
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_uncheck(self, selector, *args, **kwargs)

    Page.uncheck = _highlighted_page_uncheck

    # Wrap Locator.check/uncheck to highlight before interacting
    _orig_locator_check = Locator.check

    def _highlighted_locator_check(self, *args, **kwargs):
        _assert_visible(self.page, self, "Locator.check")
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_check(self, *args, **kwargs)

    Locator.check = _highlighted_locator_check

    _orig_locator_uncheck = Locator.uncheck

    def _highlighted_locator_uncheck(self, *args, **kwargs):
        _assert_visible(self.page, self, "Locator.uncheck")
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_uncheck(self, *args, **kwargs)

    Locator.uncheck = _highlighted_locator_uncheck

    # Wrap Page.select_option to highlight before selecting
    _orig_page_select_option = Page.select_option

    def _highlighted_page_select_option(self, selector, *args, **kwargs):
        _assert_visible(self, selector, "Page.select_option")
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_select_option(self, selector, *args, **kwargs)

    Page.select_option = _highlighted_page_select_option

    # Wrap Locator.select_option to highlight before selecting
    _orig_locator_select_option = Locator.select_option

    def _highlighted_locator_select_option(self, *args, **kwargs):
        _assert_visible(self.page, self, "Locator.select_option")
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_select_option(self, *args, **kwargs)

    # Wrap Locator.wait_for so any visible wait has a post-assertion by default.
    _orig_locator_wait_for = Locator.wait_for

    def _asserting_locator_wait_for(self, *args, **kwargs):
        result = _orig_locator_wait_for(self, *args, **kwargs)
        state = kwargs.get("state")
        if state is None and len(args) >= 1 and isinstance(args[0], str):
            state = args[0]
        if state is None and len(args) >= 2 and isinstance(args[1], str):
            state = args[1]
        if state == "visible":
            try:
                assert self.is_visible(), "Locator is not visible after wait_for(visible)"
            except Exception as exc:
                attach_screenshot(self.page, "Locator wait_for visible assertion failed", force=True)
                raise AssertionError(f"wait_for visible assertion failed: {exc}") from exc
        return result

    Locator.wait_for = _asserting_locator_wait_for

    Locator.select_option = _highlighted_locator_select_option


def before_all(context):
    """Setup browser once before all tests"""
    # Prefer shell env USER_TYPE over behave.ini userdata so terminal overrides work.
    env_user_type = os.getenv("USER_TYPE")
    userdata = getattr(context.config, "userdata", {})
    userdata_user_type = userdata.get("USER_TYPE") if hasattr(userdata, "get") else None
    user_type = (env_user_type or userdata_user_type or "student").strip().lower()
    os.environ["USER_TYPE"] = user_type
    from utils.config import Config

    global setup_complete

    context.playwright = None
    context.browser = None
    context.browser_context = None
    context.page = None
    context.setup_failed = False

    try:
        is_headless, is_ci = _resolve_headless_mode()

        browser_args = [
            '--force-device-scale-factor=1',
            '--high-dpi-support=1',
            '--disable-blink-features=AutomationControlled',
            '--use-fake-ui-for-media-stream',
            '--use-fake-device-for-media-stream',
        ]

        if is_headless:
            # Fixed window size required in headless/CI; --start-maximized is unsupported headless.
            browser_args.append('--window-size=1920,1080')
        else:
            # Maximize the browser window in local headed runs.
            browser_args.append('--start-maximized')

        # Linux CI-safe Chromium flags
        if is_ci:
            browser_args.extend([
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-software-rasterizer',
            ])

        # Start browser
        context.playwright = sync_playwright().start()

        try:
            context.browser = context.playwright.chromium.launch(
                headless=is_headless,
                slow_mo=0 if is_headless else 1500,
                args=browser_args,
            )
        except Exception as launch_exc:
            # Safety fallback: retry once in headless if local headed launch fails due missing display.
            if not is_headless:
                print(f"Headed launch failed, retrying in headless mode: {launch_exc}")
                is_headless = True
                context.browser = context.playwright.chromium.launch(
                    headless=True,
                    slow_mo=0,
                    args=browser_args,
                )
            else:
                raise

        # Headed: disable fixed viewport so --start-maximized takes full effect.
        # Headless/CI: enforce fixed 1920x1080 viewport for deterministic rendering.
        if is_headless:
            context_options = {
                "viewport": {"width": 1920, "height": 1080},
                "accept_downloads": True,
            }
        else:
            context_options = {
                "no_viewport": True,
                "accept_downloads": True,
            }

        context.browser_context = context.browser.new_context(**context_options)
        context.page = context.browser_context.new_page()
        print(
            f"Playwright launch mode: {'headless' if is_headless else 'headed'} "
            f"(CI={is_ci}, HEADLESS={os.getenv('HEADLESS')})"
        )

        _install_highlight_wrappers()

        print("\n========== STEP 2: User Login ==========")
        # Step 2: Perform login
        login_page = LoginPage(context.page)
        # Navigate back to base URL to find login button
        context.page.goto(Config.BASE_URL)
        login_page.click_login_button()
        login_page.enter_credentials(Config.USERNAME, Config.PASSWORD)
        login_page.click_sign_in_button()

        # Handle all 4 popups after login
        login_page.handle_all_popups()

        # Validate successful login
        login_page.validate_successful_login()
        print("✓ User Login Completed")

        setup_complete = True
        print("\n========== STEP 3: Running Test Scenarios ==========")
    except Exception as exc:
        context.setup_failed = True
        print(f"before_all setup failed: {exc!r}")
        print(traceback.format_exc())
        # Cleanup any partially initialized resources so hooks remain stable.
        _safe_close(getattr(context, "browser_context", None), "browser context")
        _safe_close(getattr(context, "browser", None), "browser")
        _safe_stop(getattr(context, "playwright", None))
        context.browser_context = None
        context.browser = None
        context.playwright = None
        context.page = None
        # Keep hooks alive so after_all can complete and reports can still be generated.


def before_scenario(context, scenario):
    """Skip setup scenarios as they're already done in before_all"""
    set_report_context(context)

    if getattr(context, "setup_failed", False):
        scenario.skip("Skipped because before_all setup failed")
        return

    # Tag scenarios to identify which ones to skip
    if 'Validate Guest page' in scenario.name or 'Valid login' in scenario.name:
        scenario.skip("Already executed in before_all hook")


def before_step(context, step):
    # Keep active context in helper so page methods can embed screenshots in html reports.
    set_report_context(context)


def after_step(context, step):
    # Always capture screenshot on step failure for richer Allure/HTML reporting.
    try:
        if step.status == "failed" and getattr(context, "page", None):
            safe_step_name = step.name.replace(" ", "_")[:80]
            attach_screenshot(context.page, f"FAILED_STEP_{safe_step_name}", context=context)
    except Exception as exc:
        print(f"after_step screenshot capture failed: {exc}")


def after_scenario(context, scenario):
    # Capture final state for failed scenarios too.
    try:
        if scenario.status == "failed" and getattr(context, "page", None):
            safe_scenario_name = scenario.name.replace(" ", "_")[:80]
            attach_screenshot(context.page, f"FAILED_SCENARIO_{safe_scenario_name}", context=context)
    except Exception as exc:
        print(f"after_scenario screenshot capture failed: {exc}")


def after_all(context):
    """Logout and cleanup after all tests"""
    print("\n========== STEP 4: User Logout ==========")

    try:
        # Perform logout only when a page exists
        if getattr(context, "page", None):
            login_page = LoginPage(context.page)
            login_page.logout()
            print("✓ User Logout Completed")
        else:
            print("Skipping logout: page was not initialized")
    except Exception as e:
        print(f"Logout failed or not needed: {e}")

    _safe_close(getattr(context, "browser_context", None), "browser context")
    _safe_close(getattr(context, "browser", None), "browser")
    _safe_stop(getattr(context, "playwright", None))
    print("\n========== Test Execution Complete ==========")
