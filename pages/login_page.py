from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "ap_email")
    PASSWORD = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    CONTINUE_BUTTON = (By.CLASS_NAME, "a-button-input")
    ALERT = (By.CLASS_NAME, "a-list-item")

    def fill_email_textbox(self, email):
        self.clear_text(*self.EMAIL).send_text(email, *self.EMAIL)

    def click_continue_button(self):
        self.click_element(*self.CONTINUE_BUTTON)

    def fill_password_textbox(self, password):
        self.send_text(password, *self.PASSWORD)

    def click_sign_in_button(self):
        self.click_element(*self.SIGN_IN_BUTTON)






