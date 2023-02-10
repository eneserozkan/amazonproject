from selenium.webdriver.common.by import By

from base import data
from pages.base_page import BasePage
from pages.product_page import ProductPage


class ListPage(BasePage):
    ADD_TO_LIST = (By.ID, "add-to-wishlist-button-submit")
    SHOPPING_LIST = (By.XPATH, "//span[contains(@class, 'nav-text') and normalize-space(text()) = 'Shopping List']")
    DELETE_BUTTON = (By.NAME, "submit.deleteItem")
    CONTINUE_SHOPPING_BUTTON = (By.CLASS_NAME, "//span[contains(@class,'a-button-text')]  [contains(text(),'Continue shopping')]")
    ITEM_NAME = (By.ID, "a[id*='itemName_']")

    def click_add_to_list(self):
        """The item which you selected is added to shopping list"""
        self.click_element(*self.ADD_TO_LIST)

    def click_continue_shopping(self):
        """For the continuing to the shopping, the function clicks the button."""
        self.click_element(*self.CONTINUE_SHOPPING_BUTTON)

    def click_shopping_list(self):
        """After you selected your product, it provides us to reach the shopping list"""
        self.click_element(*self.SHOPPING_LIST)

    def check_product(self):

        return self.find_element(*self.ITEM_NAME).text

    def click_delete_button(self):
        """After going to the shopping list, this function deletes the product that you added
        to the list."""
        self.click_element(*self.DELETE_BUTTON)

    def check_list_item_name(self):
        """For assertion, function checks the product name is the same both on the product page
        and shopping list page."""
        return self.find_element(self.ITEM_NAME).text

    def is_deleted_favorite_product(self):
        """Checks and returns whether the product has been deleted"""
        if not self.presence_for_element(self.DELETE_BUTTON).is_displayed():
            for index, item in enumerate(self.presence_for_all_elements(self.ITEM_NAME)):

                if data.product_title == item.get_attribute("title"):
                    return data.product_title == item.get_attribute("title")

            return False
