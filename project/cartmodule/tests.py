from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time


class CartModuleTest(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("E:\\SEPP\\Lab\\selenium\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/login/")
        username_input = self.driver.find_element_by_id("log_username")
        username_input.send_keys("yash")
        password_input = self.driver.find_element_by_id("log_password")
        password_input.send_keys("12345678")
        loginbutton = self.driver.find_element_by_id("log_loginbutton")
        loginbutton.click()
        self.driver.maximize_window()

    # def tearDown(self):
    #     self.driver.quit()

    def cartTest(self):
        driver = self.driver
        cartButton = driver.find_element_by_xpath(
            "//*[@id='content']/header/div/div/div[2]/div/div/ul/li[5]/a/i")
        cartButton.click()
        time.sleep(4)
        increaseQuantity = driver.find_element_by_xpath(
            "//*[@id='content']/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/a[2]/i")
        increaseQuantity.click()
        time.sleep(4)
        decreaseQuantity = driver.find_element_by_xpath(
            "//*[@id='content']/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/a[1]/i")
        decreaseQuantity.click()
        time.sleep(4)
        placeOrderButton = driver.find_element_by_xpath(
            "//*[@id='content']/div/div/div/div[2]/div/div/div/center/a")
        placeOrderButton.click()
        time.sleep(4)
        continueButton = driver.find_element_by_xpath(
            "//*[@id='content']/div/div[2]/a[3]")
        continueButton.click()
        time.sleep(4)
