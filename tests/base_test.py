import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = 'http://www.amazon.com/'

    def setUp(self):
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 10)
