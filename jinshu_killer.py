from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"chromedriver.exe"

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\google\\Chrome\\User Data\\")
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)  # 使用Service来指定驱动路径

driver.get("your class url")

# 等待页面加载完成
WebDriverWait(driver, 35).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/span"))
)

# 点击指定的元素
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/span").click()

tinput = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/input[1]")
sbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/input[2]")


tinput.clear()

while True:
    tinput.send_keys ('666666666666666666666666666666666666666666666666666666666666666666666666666')
    sbutton.click()
