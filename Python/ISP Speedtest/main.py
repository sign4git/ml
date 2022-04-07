from decouple import config
from selenium import webdriver
import time

PROMISED_DOWN = 300
PROMISED_UP = 300
TWITTER_EMAIL = config("TWITTER_EMAIL", default="")
TWITTER_PASSWORD = config("TWITTER_PASSWORD", default="")
CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver_win32\chromedriver.exe"
SPEEDTEST_NET = "https://www.speedtest.net/"
TWITTER_PATH = "https://twitter.com/i/flow/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = None
        self.up = None

    def get_internet_speed(self):

        self.driver.get(SPEEDTEST_NET)
        start_element = self.driver.find_element_by_class_name("start-text")
        start_element.click()
        time_now = time.time()
        time_delay = time_now + 70
        while time.time() <= time_delay:
            continue

        download_element = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload_element = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.down = float(download_element.text)
        self.up = float(upload_element.text)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_PATH)
        time.sleep(5)
        # login_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        # login_element.click()
        # time.sleep(5)
        username_element = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[1]/div')
        username_element.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        next_element = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_element.click()
        time.sleep(5)
        password_element = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label')
        password_element.send_keys(TWITTER_PASSWORD)
        time.sleep(5)
        final_login = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        final_login.click()
        time.sleep(5)
        tweet_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_element.send_keys(f"Hey ISP, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up")
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div')
        tweet_btn.click()
        time.sleep(5)


speedTwitterBot = InternetSpeedTwitterBot()
speedTwitterBot.get_internet_speed()
if speedTwitterBot.down < PROMISED_DOWN or speedTwitterBot.up < PROMISED_UP:
    speedTwitterBot.tweet_at_provider()
speedTwitterBot.driver.quit()
