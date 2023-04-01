from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get('https://kd.nsfc.gov.cn/finalSearchList?s=%E4%BA%A7%E5%93%81%E8%B4%A8%E9%87%8F ')
wait = WebDriverWait(driver, 5)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/div[2]/div/button[2]')))
while True:
    time.sleep(10)
    button.click()

# 在这里可以添加其他操作，例如获取页面元素等

# 关闭浏览器
driver.quit()
