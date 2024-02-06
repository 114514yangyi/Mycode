from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

# Specify the path to the ChromeDriver executable
path = '/home/huyang/Document/python-project/chromedriver'
chrome_options.add_argument("executable_path="+path)
# Instantiate the Chrome webdriver with the options object
browser = webdriver.Chrome(options=chrome_options)

url="https://www.baidu.com"

browser.get(url)

button=browser.find_element(by=By.ID,value="su")
button=browser.find_elements(by=By.XPATH,value="//input[@id='su']")
print(button)
content=browser.page_source




