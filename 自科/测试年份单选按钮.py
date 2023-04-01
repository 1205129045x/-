from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# 初始化WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=0')
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get('https://kd.nsfc.gov.cn/finalSearchList?s=%E8%B4%A8%E9%87%8F')
wait = WebDriverWait(driver, 10)
base_xpath = "//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']//div[@class='container_list_left']/div[1]/div[@role='tablist']//div[@role='tabpanel']//ul[@class='scrollbar']/li[{0}]/div[@role='radiogroup']/label[@role='radio']//span[@class='el-radio__inner']"

# 循环点击按钮
for i in range(2, 6):
    xpath = base_xpath.format(i)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    # time.sleep(5)
    button.click()
# 2021年button //div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']//div[@class='container_list_left']/div[1]/div[@role='tablist']//div[@role='tabpanel']//ul[@class='scrollbar']/li[2]/div[@role='radiogroup']/label[@role='radio']//span[@class='el-radio__inner']
# 2020年button //div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']//div[@class='container_list_left']/div[1]/div[@role='tablist']//div[@role='tabpanel']//ul[@class='scrollbar']/li[3]/div[@role='radiogroup']/label[@role='radio']//span[@class='el-radio__inner']
time.sleep(5)
driver.quit()