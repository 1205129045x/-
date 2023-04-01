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
base_xpath = "//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']//div[@class='container_list_left']/div[1]/div[@role='tablist']//div[@role='tabpanel']//ul[@class='scrollbar']/li[{0}]/div[@role='radiogroup']/label[@role='radio']//span[@class='el-radio__inner']"

# 循环点击年份按钮
for i in range(2, 6): #从2开始是因为2021年的按钮编号是2，然后依次随着数字变大年份变小
    xpath = base_xpath.format(i)
    button_year = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    button_year.click()
    time.sleep(2)
    # while True 循环遍历当前年度下的所有页数
    while True:
        # elements 为当前页的10个项目信息 一次性获取，然后遍历输入到csv中
        elements = driver.find_elements(By.XPATH, "//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='Waiting']/div")
        for element in elements:
            if element.text == '':
                continue
            print(element.text)
            rows = element.text.split('\n')
            filename = f"data质量_{i}.csv"
            with open(filename, 'a', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                writer.writerow(rows)
        try: # 进行下一页的判断
            # 如果遇到超时异常，则说明已经遍历到了最后一页，可以跳出循环
            button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='el-pagination is-background']/button[2]")))
            # button是下一页按钮
            button.click()
        except TimeoutException:
            break
        else:
            time.sleep(2)
            

# 关闭浏览器
driver.quit()
