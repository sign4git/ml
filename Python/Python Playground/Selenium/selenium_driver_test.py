from selenium import webdriver
import datetime


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
website = driver.get("https://www.python.org/")
event_list = driver.find_element_by_css_selector(
    "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul")
print((event_list.text.splitlines()))

event_date = []
event_name = []

for current_text in event_list.text.splitlines():
    isDate = validate(current_text)
    if isDate:
        print("in if")
        event_date.append(current_text)
    else:
        print("in else")
        event_name.append(current_text)
print(event_name)
print(event_date)

event_dict = {}

for i in range(0, len(event_date)):
    event_dict[i] = {
        "name": event_name[i],
        "time": event_date[i]
    }
print(event_dict)
driver.quit()
