from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time
# Create your tests here.


class HomeModuleTest(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("E:\\selenium\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/index/")

    def tearDown(self):
        self.driver.quit()

    def orderNowTest(self):
        driver = self.driver
        orderNowButton = driver.find_element_by_id("orderNow")
        orderNowButton.click()

    def orderNow1Test(self):
        driver = self.driver
        orderNowButton = driver.find_element_by_id("orderNow1")
        driver.implicitly_wait(8)
        orderNowButton.click()

    def offerItemTest(self):
        driver = self.driver
        driver.execute_script(
            "window.scrollTo(0, 600);")
        time.sleep(4)
        itembutton = driver.find_element_by_xpath(
            "//*[@id='content']/section/div/div/div[2]/div/div/div/div[1]/div/div[6]/div/div[1]/div/figure/a/img")
        itembutton.click()
        # time.sleep(4)

    def feedbackFormTest(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,3000);")
        name_input = driver.find_element_by_id("feed_name")
        name_input.send_keys("test")
        email_input = driver.find_element_by_id("feed_email")
        email_input.send_keys("test@gmail.com")
        # phone_input = driver.find_element_by_id("feed_phone")
        # phone_input.send_keys("88661626")#wrong mobile number
        # phone_input.send_keys("8818181818")
        msg_input = driver.find_element_by_id("feed_message")
        msg_input.send_keys("your website is so user friendly....")
        send = driver.find_element_by_id("feed_send")
        send.click()

    def sidebarTest(self):
        driver = self.driver
        sidebar = driver.find_element_by_xpath("//*[@id='sidebarCollapse']")
        driver.implicitly_wait(10)
        sidebar.click()
        time.sleep(10)
        sidebarClose = driver.find_element_by_id("dismiss")
        sidebarClose.click()

    def sidebarOptionTest(self):
        driver = self.driver
        sidebar = driver.find_element_by_xpath("//*[@id='sidebarCollapse']")
        driver.implicitly_wait(10)
        sidebar.click()
        time.sleep(6)
        homeOption = driver.find_element_by_xpath(
            "//*[@id='mCSB_1_container']/ul/li[1]/a")
        homeOption.click()

    def homeFooterTest(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(4)
        home = driver.find_element_by_xpath(
            "//*[@id='content']/i/footer/div/div[1]/div[2]/div[2]/ul/li[1]/a")
        home.click()
