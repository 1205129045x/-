from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# 初始化WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=0')
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get('https://kd.nsfc.gov.cn/finalSearchList?s=%E4%BA%A7%E5%93%81%E8%B4%A8%E9%87%8F')
wait = WebDriverWait(driver, 10)

html = driver.page_source
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# elements = soup.select("//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='Waiting']/div")
# for element in elements:
    # print(element.text)
elements = driver.find_elements(By.XPATH, "//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='Waiting']/div")
for element in elements:
    print(element.text)
driver.quit()