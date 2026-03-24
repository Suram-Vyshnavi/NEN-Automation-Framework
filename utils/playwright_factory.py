from playwright.sync_api import sync_playwright
from config.env_config import HEADLESS

class PlaywrightFactory:
    def start(self):
        pw = sync_playwright().start()
        browser = pw.chromium.launch(
            headless=HEADLESS,
            args=[
                '--start-maximized',
                '--force-device-scale-factor=1',  # Fix DPI scaling issues
                '--high-dpi-support=1',
                '--use-fake-ui-for-media-stream',
                '--use-fake-device-for-media-stream'
            ]
        )
        context = browser.new_context(
            permissions=[],
            no_viewport=True  # Let browser use full window size without scaling
        )
        page = context.new_page()
        
        return pw, browser, context, page