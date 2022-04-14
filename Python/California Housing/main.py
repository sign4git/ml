import requests
from bs4 import BeautifulSoup
from selenium import webdriver

CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver_win32\chromedriver.exe"
FORMS_URL = 'https://forms.gle/dK9QXivrzSfDcDNQ6'
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
             '%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A' \
             '-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C' \
             '%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A' \
             '%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse' \
             '%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B' \
             '%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D' \
             '%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min' \
             '%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D '

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.75 Safari/537.36 "
}

response = requests.get(ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
anchor_link_list = soup.find_all(name='a', class_='list-card-link list-card-link-top-margin')
address_list = soup.find_all(name='address', class_='list-card-addr')
price_list = soup.find_all(class_='list-card-price', name='div')
print(address_list[0])

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
for i in range(len(anchor_link_list)):
    driver.get(FORMS_URL)
    address_box = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_box.send_keys(address_list[i].getText())
    price_box = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box.send_keys(price_list[i].getText().replace("/mo", ""))
    property_link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(anchor_link_list[i]['href'])
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()

driver.quit()
