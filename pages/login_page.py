from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert True

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True

    def should_be_login_url(self):
        assert "login" in self.browser.current_url
