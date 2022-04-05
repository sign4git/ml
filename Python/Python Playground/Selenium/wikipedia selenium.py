from selenium import webdriver

CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
website = driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count_element = driver.find_element_by_css_selector("#articlecount > a:nth-child(1)")
print(article_count_element.text)
