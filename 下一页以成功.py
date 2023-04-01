from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开网页
driver.get("https://kd.nsfc.gov.cn/finalSearchList?s=%E4%BA%A7%E5%93%81%E8%B4%A8%E9%87%8F")

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='pagination']/ul/li[last()]")))

# 查找元素并模拟点击


while True:
    button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='app']/div[@class='app-wrapper']/div[@class='main-container']/div[@class='container_main']//div[@class='el-pagination is-background']/button[2]")))
    if not button:
        break
    button.click()
    time.sleep(10)
# 关闭浏览器
driver.quit()
