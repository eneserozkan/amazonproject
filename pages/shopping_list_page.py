from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ListPage(BasePage):
    ADD_TO_LIST = (By.ID, "add-to-wishlist-button-submit")
    SHOPPING_LIST = (By.XPATH, "//span[contains(@class, 'nav-text') and normalize-space(text()) = 'Shopping List']")
    DELETE_BUTTON = (By.ID, "delete-button-I16KQMRGE20EPI")
    item_name = (By.ID, "itemName_I16KQMRGE20EPI")

    def click_add_to_list(self):
        self.click_element(*self.ADD_TO_LIST)

    def check_product(self):
        return self.find_element(*self.item_name).text

    def click_shopping_list(self):
        self.click_element(*self.SHOPPING_LIST)

    def click_delete_button(self):
        self.click_element(*self.DELETE_BUTTON)

