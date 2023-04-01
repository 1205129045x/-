from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
# 初始化WebDriver
driver = webdriver.Chrome()

# 打开网页
driver.get('https://kd.nsfc.gov.cn/finalSearchList?s=%E4%BA%A7%E5%93%81%E8%B4%A8%E9%87%8F')
wait = WebDriverWait(driver, 5)

html = driver.page_source
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# elements = soup.select("//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='Waiting']/div")
# for element in elements:
    # print(element.text)
elements = soup.find_all('div', {'id': 'app'})[0] \
                  .find_all('div', {'class': 'app-wrapper'})[0] \
                  .find_all('div', {'class': 'main-container'})[0] \
                  .find_all('div', {'class': 'container_main'})[0] \
                  .find_all('div', {'class': 'Waiting'})[0] \
                  .find_all('div')
for element in elements:
    print(element.text)
driver.quit()