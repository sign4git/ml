from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
website = driver.get("http://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element_by_name("fName")
fName.send_keys("First")
lName = driver.find_element_by_name("lName")
lName.send_keys("Last")
email = driver.find_element_by_name("email")
email.send_keys("email@email.com")
btn = driver.find_element_by_tag_name("button")
btn.send_keys(Keys.ENTER)
