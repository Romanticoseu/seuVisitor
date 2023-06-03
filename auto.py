from selenium import webdriver
from selenium.webdriver.chrome.service import Service

webdriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
service = Service(webdriver_path)

driver = webdriver.Chrome(service=service)

driver.get('https://infoplus.seu.edu.cn/infoplus/form/XWJXSQ/start?sig=bd12f0a41c7a9b8a2a2d0cbd48b138dc&ts=1767024000&uid=0f1fb840-aa02-11ea-b752-005056bd7aba&lxfs=18351939811')

# 其他操作...

# driver.quit()
