from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    SECOND_PAGE = (By.CSS_SELECTOR, "a[aria-label='Go to page 2']")
    THIRD_PRODUCT = (By.CSS_SELECTOR, "[data-component-type='s-product-image'] > a")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[cel_widget_id*='MAIN-SEARCH'] h2")
    SEARCH_TEXT_ELEMENT = (By.CSS_SELECTOR, "[data-component-type='s-result-info-bar'] span")
    SELECT_PAGINATION = (By.CLASS_NAME, "s-pagination-selected")

    def click_second_page(self):
        self.click_element(*self.SECOND_PAGE)

    def check_second_page(self):
        return self.presence_for_element(self.SELECT_PAGINATION).text == "2"

    def click_third_product(self):
        self.click_element(*self.THIRD_PRODUCT)

    def click_third_page(self):
        self.presence_for_all_elements(self.THIRD_PRODUCT)[2].click()
