import time

from base import data
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.shopping_list_page import ListPage
from tests.base_test import BaseTest


class TestCheckAmazonWeb(BaseTest):
    valid_mail = "*******@gmail.com"
    valid_password = "*******"
    category_name = "Samsung"

    def test_check_amazon_web(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()

        login_page = LoginPage(self.driver)
        login_page.fill_email_textbox(data.email)
        login_page.click_continue_button()
        login_page.fill_password_textbox(data.password)
        login_page.click_sign_in_button()
        home_page.check_main_page()

        home_page.fill_search_box(data.search_keyword)
        home_page.click_search_button()
        assert home_page.is_correct_search(), "Search result is uncorrect!"
        time.sleep(2)

        product_page = ProductPage(self.driver)
        product_page.click_second_page()
        product_page.click_third_product()
        assert product_page.is_on_second_page(), "Not on page 2"

        list_page = ListPage(self.driver)
        base_test = BaseTest(self.driver)
        list_page.click_add_to_list()
        list_page.click_continue_shopping()
        list_page.click_shopping_list()
        self.assertEqual(product_page.product_text(), list_page.check_list_item_name(), "It is not correct!")
        list_page.click_delete_button()
        assert not list_page.is_deleted_favorite_product(), "The product has not been deleted from the list"

    def tearDown(self):
        self.driver.quit()
