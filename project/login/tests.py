from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
# Create your tests here.


class LoginTest(LiveServerTestCase):

    def setUp(self):
        self.driver = Chrome("E:\\SEPP\\Lab\\selenium\\chromedriver.exe")

    def tearDown(self):
        self.driver.quit()

    def loginFormTest(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/login')
        username_input = driver.find_element_by_id("log_username")
        username_input.send_keys("yash")
        password_input = driver.find_element_by_id("log_password")
        password_input.send_keys("12345678")
        loginbutton = driver.find_element_by_id("log_loginbutton")
        loginbutton.click()

    def registerFormTest(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/login/register')
        username_input = driver.find_element_by_id(
            "reg_username")
        email_input = driver.find_element_by_id("reg_email")
        username_input.send_keys("yash")
        email_input.send_keys("yash@gmail.com")
        password_input = driver.find_element_by_id("reg_password")
        password_input.send_keys('12345678')
        password1_input = driver.find_element_by_id("reg_password1")
        password1_input.send_keys('12345678')
        register = driver.find_element_by_id("reg_registerbutton")
        register.click()
