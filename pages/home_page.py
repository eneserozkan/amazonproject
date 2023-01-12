from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SIGN_PART = (By.ID, "nav-link-accountList-nav-line-1")  # list için önce buraya tıklanacak sonra liste
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    home_page = (By.CSS_SELECTOR, "[role='main']")

    def check_logo(self):
        return self.presence_for_element(*self.home_page).is_displayed()

    def click_sign_in(self):
        self.click_element(*self.SIGN_PART)

    def fill_search_box(self, name):
        self.send_text(name, *self.SEARCH_BOX)

    def click_search_button(self):
        self.click_element(*self.SEARCH_BUTTON)
