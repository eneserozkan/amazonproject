from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SIGN_PART = (By.ID, "nav-link-accountList-nav-line-1")  # list için önce buraya tıklanacak sonra liste
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    CHECK_HOME_PAGE = (By.ID, "nav-logo-sprites")
    SEARCH_TEXT_ELEMENT = (By.CSS_SELECTOR, "[data-component-type='s-result-info-bar'] span")
    home_page = (By.CSS_SELECTOR, "[role='main']")

    def check_main_page(self):
        """Checks the main page whether the user is in or not"""
        return self.presence_for_element(*self.home_page).is_displayed()

    def click_sign_in(self):
        """click sign in button"""
        self.click_element(*self.SIGN_PART)

    def fill_search_box(self, name):
        """Searches for keywords via the search bar"""
        self.send_text(name, *self.SEARCH_BOX)

    def click_search_button(self):
        """Click search button"""
        self.click_element(*self.SEARCH_BUTTON)

    def check_main_page(self):
        """Assert for main page"""
        assert isinstance(self.find_element(*self.CHECK_HOME_PAGE).text, object)

    def check_search_name(self):
        """Checks the search name is correct or not."""

        return self.presence_for_all_elements(self.SEARCH_TEXT_ELEMENT)[2].text.strip('"') == "samsung"

