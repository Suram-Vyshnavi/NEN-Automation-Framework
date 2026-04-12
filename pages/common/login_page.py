from locators.common.login_locators import LoginLocators
from utils.helpers import attach_screenshot, highlight_element


class LoginPage:
	def __init__(self, page):
		self.page = page
		self.locators = LoginLocators()

	def click_login_button(self):
		try:
			login_btn = self.page.locator(self.locators.LOGIN_BUTTON)
			login_btn.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.LOGIN_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Click Login Button Failed")
			print(f"Failed to click login button: {e}")
	def enter_credentials(self, email, password):
		try:
			email_input = self.page.locator(self.locators.EMAIL_INPUT)
			email_input.wait_for(state="visible", timeout=10000)
			self.page.fill(self.locators.EMAIL_INPUT, email)
			highlight_element(self.page, self.locators.EMAIL_INPUT)

			password_input = self.page.locator(self.locators.PASSWORD_INPUT)
			password_input.wait_for(state="visible", timeout=10000)
			self.page.fill(self.locators.PASSWORD_INPUT, password)
			highlight_element(self.page, self.locators.PASSWORD_INPUT)

		except Exception as e:
			attach_screenshot(self.page, "Enter Credentials Failed")
			print(f"Failed to enter credentials: {e}")
	def click_sign_in_button(self):
		try:
			sign_in_btn = self.page.locator(self.locators.SIGN_IN)
			sign_in_btn.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.SIGN_IN)
		except Exception as e:
			attach_screenshot(self.page, "Click Sign In Button Failed")
			print(f"Failed to click sign in button: {e}")
	def handle_no_thanks_popup(self):
		try:
			no_thanks_btn = self.page.locator(self.locators.NO_THANKS_POPUP)
			no_thanks_btn.wait_for(state="visible", timeout=5000)
			if no_thanks_btn.is_visible():
				self.page.click(self.locators.NO_THANKS_POPUP)
		except Exception:
			pass

	def handle_get_started_popup(self):
		try:
			close_btn = self.page.locator(self.locators.CLOSE_POPUP_GETSTARTED)
			close_btn.wait_for(state="visible", timeout=5000)
			if close_btn.is_visible():
				self.page.click(self.locators.CLOSE_POPUP_GETSTARTED)
		except Exception:
			pass

	def handle_start_journey_popup(self):
		try:
			journey_popup = self.page.locator(self.locators.START_YOUR_JOURNEY_POPUP)
			journey_popup.wait_for(state="visible", timeout=10000)
			if journey_popup.is_visible():
				highlight_element(self.page, self.locators.START_YOUR_JOURNEY_POPUP)
				next_btn = self.page.locator(self.locators.NEXT_BUTTON)
				next_btn.wait_for(state="visible", timeout=5000)
				self.page.click(self.locators.NEXT_BUTTON)
		except Exception:
			attach_screenshot(self.page, "Popup 2: Not Found - Continuing")

	def handle_personalised_journey_popup(self):
		try:
			personalised_popup = self.page.locator(self.locators.CREATE_PERSONALISED_JOURNEY_POPUP)
			personalised_popup.wait_for(state="visible", timeout=10000)
			if personalised_popup.is_visible():
				highlight_element(self.page, self.locators.CREATE_PERSONALISED_JOURNEY_POPUP)
				next_btn = self.page.locator(self.locators.NEXT_BUTTON)
				next_btn.wait_for(state="visible", timeout=5000)
				self.page.click(self.locators.NEXT_BUTTON)
		except Exception:
			attach_screenshot(self.page, "Popup 3: Not Found - Continuing")

	def handle_start_program_journey_popup(self):
		try:
			start_journey_btn = self.page.locator(self.locators.START_PROGRAM_JOURNEY_BUTTON)
			start_journey_btn.wait_for(state="visible", timeout=10000)
			if start_journey_btn.is_visible():
				highlight_element(self.page, self.locators.START_PROGRAM_JOURNEY_BUTTON)
				self.page.click(self.locators.START_PROGRAM_JOURNEY_BUTTON)
		except Exception:
			attach_screenshot(self.page, "Popup 4: Not Found - Continuing")

	def handle_all_popups(self):
		self.handle_no_thanks_popup()
		self.handle_start_journey_popup()
		self.handle_personalised_journey_popup()
		self.handle_start_program_journey_popup()
		self.handle_get_started_popup()

	def validate_successful_login(self):
		try:
			home_element = self.page.locator(self.locators.VALIDATE_LOGO)
			home_element.wait_for(state="visible", timeout=15000)
			assert home_element.is_visible(), "Home element is not visible - Login may have failed"
			highlight_element(self.page, self.locators.VALIDATE_LOGO)
		except Exception as e:
			attach_screenshot(self.page, "Login Validation Failed")
			print(f"Login validation failed: {e}")
	def logout(self):
		try:
			if hasattr(self.locators, "PROFILE_MENU"):
				try:
					profile_menu = self.page.locator(self.locators.PROFILE_MENU)
					profile_menu.wait_for(state="visible", timeout=5000)
					self.page.click(self.locators.PROFILE_MENU)
				except Exception:
					pass
			logout_btn = self.page.locator(self.locators.LOGOUT_BUTTON)
			logout_btn.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.LOGOUT_BUTTON)
		except Exception as exc:
			attach_screenshot(self.page, "Logout Failed or Button Not Found")
			print(f"Logout failed: {exc}")

