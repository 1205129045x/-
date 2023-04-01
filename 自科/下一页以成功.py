from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

options = webdriver.ChromeOptions()
# 初始化浏览器驱动
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get("https://kd.nsfc.gov.cn/finalSearchList?s=%E8%B4%A8%E9%87%8F")

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
time.sleep(5)
# 查找元素并模拟点击


while True:

    elements = driver.find_elements(By.XPATH, "//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='Waiting']/div")
    for element in elements:
        if element.text == '':
            continue
        print(element.text)
        rows = element.text.split('\n')
        with open('data质量.csv', 'a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(rows)
    # 等待下一个按钮出现并点击它
    try:
        # 如果遇到超时异常，则说明已经遍历到了最后一页，可以跳出循环
        button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='el-pagination is-background']/button[2]")))
        button.click()
    except TimeoutException:
        break
    else:
        time.sleep(5)
# 关闭浏览器
driver.quit()
