from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')  # 启用无头模式
chrome_options.add_argument('--no-sandbox')  # 必须添加此选项，否则在Linux服务器上可能会遇到权限问题

webdriver_path = '/path/to/chromedriver'  # 指定ChromeDriver的路径
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

driver.get('https://infoplus.seu.edu.cn/infoplus/form/XWJXSQ/start?sig=bd12f0a41c7a9b8a2a2d0cbd48b138dc&ts=1767024000&uid=0f1fb840-aa02-11ea-b752-005056bd7aba&lxfs=18351939811')

# 其他操作...

driver.quit()
