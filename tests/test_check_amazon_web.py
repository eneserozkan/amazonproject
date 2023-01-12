import time
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.shopping_list_page import ListPage
from tests.base_test import BaseTest


class TestCheckAmazonWeb(BaseTest):
    valid_mail = "*****@gmail.com"
    valid_password = "*******"
    category_name = "Samsung"

    def test_check_amazon_web(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()

        login_page = LoginPage(self.driver)
        login_page.fill_email_textbox(self.valid_mail)
        login_page.click_continue_button()
        login_page.fill_password_textbox(self.valid_password)
        login_page.click_sign_in_button()

        home_page.fill_search_box(self.category_name)
        home_page.click_search_button()
        time.sleep(2)

        product_page = ProductPage(self.driver)
        product_page.click_second_page()
        product_page.click_third_product()

        list_page = ListPage(self.driver)
        list_page.click_add_to_list()
        list_page.click_shopping_list()
        list_page.click_delete_button()

    def tearDown(self):
        self.driver.quit()
