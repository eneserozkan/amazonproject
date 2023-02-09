from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    SECOND_PAGE = (By.CSS_SELECTOR, "a[aria-label='Go to page 2']")
    THIRD_PRODUCT = (By.CSS_SELECTOR, "[data-component-type='s-product-image'] > a")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[cel_widget_id*='MAIN-SEARCH'] h2")
    SEARCH_TEXT_ELEMENT = (By.CSS_SELECTOR, "[data-component-type='s-result-info-bar'] span")
    SELECT_PAGINATION = (By.CLASS_NAME, "s-pagination-selected")

    def click_second_page(self):
        """After you filled the searchbox's item name that you want to search,
        this function provides us to click the second page of the product you search."""
        self.click_element(*self.SECOND_PAGE)

    def check_second_page(self):
        """Assert you are on the 2 page."""
        return self.presence_for_element(self.SELECT_PAGINATION).text == "2"

    def product_text(self):
        """For the assertion, this function takes the product name that you select"""
        return self.find_element(self.PRODUCT_TITLE)[2].text

    def click_third_product(self):
        """Select third product on product page."""
        self.presence_for_all_elements(self.THIRD_PRODUCT)[2].click()

    def is_on_second_page(self):
        """For assertion, this function checks whether the user is on the 2nd page or not"""
        return self.presence_for_element(self.SELECT_PAGINATION).text == "2"
