from decouple import config
from selenium import webdriver
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = config("SIMILAR_ACCOUNT", default="")
INSTA_USERNAME = config("INSTA_USERNAME", default="")
INSTA_PWD = config("INSTA_PWD", default="")
INSTA_LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(INSTA_LOGIN_URL)
        time.sleep(3)
        username_element = self.driver.find_element_by_name('username')
        username_element.send_keys(INSTA_USERNAME)
        password_element = self.driver.find_element_by_name("password")
        password_element.send_keys(INSTA_PWD)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        time.sleep(3)
        not_now_element = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/section/main/div/div/div/div/button')
        not_now_element.click()
        time.sleep(5)
        not_now_element_2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now_element_2.click()

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(3)
        following_element = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[3]/a')
        following_element.click()
        time.sleep(5)
        bar = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bar)
            time.sleep(3)

    def follow(self):
        follow_list = self.driver.find_elements_by_class_name("wo9IH")
        for i in range(1, len(follow_list) + 1):
            print(i)
            try:
                follow_btn = self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div/div/div/div[3]/ul/div/li[{i}]/div/div[2]/button')
                follow_btn.click()
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
            time.sleep(1)


instaObj = InstaFollower()
instaObj.login()
instaObj.find_followers()
instaObj.follow()
instaObj.driver.quit()
