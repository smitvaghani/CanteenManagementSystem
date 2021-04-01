from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time


class OrderModuleTest(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("E:\\selenium\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/login/")
        username_input = self.driver.find_element_by_id("log_username")
        username_input.send_keys("yash")
        password_input = self.driver.find_element_by_id("log_password")
        password_input.send_keys("12345678")
        loginbutton = self.driver.find_element_by_id("log_loginbutton")
        loginbutton.click()

    def tearDown(self):
        self.driver.quit()

    def categoryTest(self):
        driver = self.driver
        orderNowButton = driver.find_element_by_id("orderNow")
        orderNowButton.click()  # click on order now
        category = driver.find_element_by_xpath(
            "//*[@id='content']/section/div/div/div[1]/div/a")
        category.click()  # click on category
        time.sleep(4)
        item = driver.find_element_by_xpath(
            "//*[@id='content']/div[2]/div/div/div")
        item.click()  # click on item
        time.sleep(4)
        addToCart = driver.find_element_by_xpath(
            "//*[@id='content']/div/div/div/div[2]/a")
        addToCart.click()  # click on add to cart button
        time.sleep(4)
        # driver.switch_to_alert().accept()  # accept alert box
        # time.sleep(4)
