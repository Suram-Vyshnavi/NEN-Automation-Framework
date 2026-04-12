from locators.common.messages_and_discussions_locators import Messages_and_discussionsLocators
from utils.config import Config
from utils.helpers import attach_screenshot


class ChatPage:
	def __init__(self, page):
		self.page = page
		self.locators = Messages_and_discussionsLocators()

	def click_chat_icon(self):
		try:
			self.page.locator(self.locators.CHAT_ICON).wait_for(state="visible", timeout=20000)
			self.page.click(self.locators.CHAT_ICON)
		except Exception as e:
			attach_screenshot(self.page, "Click Chat Icon Failed")
			print(f"Failed to click chat icon: {e}")
	def click_send_message_button(self):
		try:
			self.page.locator(self.locators.SEND_MESSAGE_BUTTON).wait_for(state="visible", timeout=15000)
			self.page.click(self.locators.SEND_MESSAGE_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Click Send Message Button Failed")
			print(f"Failed to click send message button: {e}")
	def click_first_contact(self):
		try:
			self.page.wait_for_timeout(5000)
			self.page.locator(self.locators.FIRST_NEW_MESSAGE).wait_for(state="visible", timeout=15000)
			self.page.click(self.locators.FIRST_NEW_MESSAGE)
		except Exception as e:
			attach_screenshot(self.page, "Click First Contact Failed")
			print(f"Failed to click first contact: {e}")
	def send_message(self, message_text=None):
		try:
			if message_text is None:
				message_text = Config.MESSAGE_TEXT
			self.page.locator(self.locators.MESSAGE_TEXTAREA).wait_for(state="visible", timeout=15000)
			self.page.fill(self.locators.MESSAGE_TEXTAREA, message_text)
			self.page.locator(self.locators.SEND_MESSAGE_ICON).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.SEND_MESSAGE_ICON)
		except Exception as e:
			attach_screenshot(self.page, "Send Message Failed")
			print(f"Failed to send message: {e}")
	def validate_latest_text_message(self):
		try:
			self.page.locator(self.locators.LATEST_SENT_MESSAGE).wait_for(state="visible", timeout=15000)
			latest_message = self.page.locator(self.locators.LATEST_SENT_MESSAGE).first
			assert latest_message.is_visible(), f"Latest sent text message '{Config.MESSAGE_TEXT}' is not visible"
			message_text = latest_message.inner_text()
			return True
		except Exception as e:
			attach_screenshot(self.page, "Validate Latest Text Message Failed")
			print(f"Latest text message validation failed: {e}")
	def validate_latest_image(self):
		try:
			self.page.locator(self.locators.LATEST_SENT_IMAGE).wait_for(state="visible", timeout=15000)
			latest_image = self.page.locator(self.locators.LATEST_SENT_IMAGE).first
			assert latest_image.is_visible(), "Latest sent image is not visible"
			return True
		except Exception as e:
			attach_screenshot(self.page, "Validate Latest Image Failed")
			print(f"Latest image validation failed: {e}")
	def validate_latest_document(self):
		try:
			self.page.locator(self.locators.LATEST_SENT_DOCUMENT).wait_for(state="visible", timeout=15000)
			latest_document = self.page.locator(self.locators.LATEST_SENT_DOCUMENT).first
			assert latest_document.is_visible(), "Latest sent document is not visible"
			return True
		except Exception as e:
			attach_screenshot(self.page, "Validate Latest Document Failed")
			print(f"Latest document validation failed: {e}")
	def click_file_upload_button(self):
		try:
			self.page.locator(self.locators.FILE_UPLOAD_BUTTON).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.FILE_UPLOAD_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Click File Upload Button Failed")
			print(f"Failed to click file upload button: {e}")
	def upload_photo(self, photo_path):
		try:
			self.page.locator(self.locators.IMAGE_OPTION).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.IMAGE_OPTION)
			file_input = self.page.locator("input[type='file']").last
			file_input.set_input_files(photo_path)
			self.page.locator(self.locators.SEND_MESSAGE_ICON).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.SEND_MESSAGE_ICON)
			self.validate_latest_image()
		except Exception as e:
			attach_screenshot(self.page, "Upload Photo Failed")
			print(f"Failed to upload photo: {e}")
	def upload_document(self, document_path):
		try:
			self.page.locator(self.locators.DOCUMENT_OPTION).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.DOCUMENT_OPTION)
			file_input = self.page.locator("input[type='file']").first
			file_input.set_input_files(document_path)
			self.page.locator(self.locators.SEND_MESSAGE_ICON).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.SEND_MESSAGE_ICON)
			self.validate_latest_document()
		except Exception as e:
			attach_screenshot(self.page, "Upload Document Failed")
			print(f"Failed to upload document: {e}")
