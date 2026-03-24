import allure
from allure_commons.types import AttachmentType
from utils.playwright_factory import PlaywrightFactory
def before_scenario(context,scenario):
    factory=PlaywrightFactory()
    context.playwright,context.browser,context.context,context.page=factory.start()
def after_scenario(context,scenario):
    if scenario.status=="passed":
        allure.attach(context.page.screenshot(),name="Success Screenshot",attachment_type=AttachmentType.PNG)
    if scenario.status=="failed":
        allure.attach(context.page.screenshot(),name="Failure Screenshot",attachment_type=AttachmentType.PNG)
    context.context.close()
    context.browser.close()
    context.playwright.stop()
