from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')

# Specify the path to the ChromeDriver executable
path = '/home/huyang/Document/python-project/chromedriver'
chrome_options.add_argument('executable_path='+path)
# Instantiate the Chrome webdriver with the options object
browser = webdriver.Chrome(options=chrome_options)


url="https://www.baidu.com"

browser.get(url)

input_text=browser.find_element(by=By.ID,value="kw")

button=browser.find_element(by=By.ID,value="su")

input_text.send_keys("周杰伦")

time.sleep(2)

button.click()

time.sleep(2)


js_buttom="document.documentElement.scrollTop=10000"

browser.execute_script(js_buttom)

time.sleep(2)

next_page=browser.find_element(by=By.XPATH,value="//a[@class='n']")

next_page.click()

time.sleep(2)

browser.back()

time.sleep(2)

browser.forward()

time.sleep(2)

browser.quit()

input()


