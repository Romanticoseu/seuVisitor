from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
import time
import config            # 需要config.py 存储数据库连接信息


class UserInfo:
    def __init__(self, id, name, phone, id_number, car_number, phone_teacher, id_department, department, id_teacher,
                 name_teacher, dormitory, card):
        self.id = id
        self.name = name
        self.phone = phone
        self.id_number = id_number
        self.car_number = car_number
        self.phone_teacher = phone_teacher
        self.id_department = id_department
        self.department = department
        self.id_teacher = id_teacher
        self.name_teacher = name_teacher
        self.dormitory = dormitory
        self.card = card

# 建立数据库连接
cnx = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)

# 创建游标对象
cursor = cnx.cursor()

# 执行SQL查询语句
query = "SELECT * FROM user_info"
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 存储数据的列表
user_info_list = []

# 将查询结果转化为UserInfo对象并存储
for row in results:
    user_info = UserInfo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
    user_info_list.append(user_info)

# 关闭游标和数据库连接
cursor.close()
cnx.close()

# 打印存储的UserInfo对象
for user_info in user_info_list:
    print(user_info.name_teacher)

def apply_car(user):
    # # Turn Chrome into headless
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome()
    url = 'https://infoplus.seu.edu.cn/infoplus/form/XWJXSQ/start?sig=bd12f0a41c7a9b8a2a2d0cbd48b138dc&ts=1767024000&uid=0f1fb840-aa02-11ea-b752-005056bd7aba&lxfs=18351939811'
    browser.get(url)
    browser.implicitly_wait(15)  # 可以用这个加快速度，少等待
    process_1 = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
    process_1.click()
    process_2 = browser.find_element(By.XPATH, '//a[@id="preview_start_button"]')
    process_2.click()

    print('Login finished, The process starts now...')
    parents_inside = browser.find_element(By.XPATH, '//tr[15]//input[@id="V1_CTRL390"]')
    parents_inside.click()
    phone_number = browser.find_element(By.XPATH, '//tr[20]//div//input[@name = "fieldLXFS"]')

    phone_number.clear()

    time.sleep(5)
    phone_number.send_keys(user.phone)

    name_student = browser.find_element(By.XPATH, '//*[@id="V1_CTRL177"]')
    name_student.clear()
    browser.execute_script("arguments[0].value = '{}';".format(user.name), name_student)

    name_university = browser.find_element(By.XPATH, '//*[@id="V1_CTRL178"]')
    name_university.clear()
    browser.execute_script("arguments[0].value = '东南大学';", name_university)

    id_student = browser.find_element(By.XPATH, '//*[@id="V1_CTRL180"]')
    id_student.clear()
    browser.execute_script("arguments[0].value = '{}';".format(user.id_number), id_student)

    #将界面拉到最下面，这个很关键的
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    button_1 = browser.find_elements(By.XPATH, '//tr//input[@id="V1_CTRL267"]')
    for i in button_1:
        browser.execute_script("arguments[0].click();", i)

    campus = browser.find_elements(By.XPATH, '//tr[33]//td[4]//input[@id  = "V1_CTRL274"]')
    for i in campus:
        browser.execute_script("arguments[0].click();", i)

    drive_or_not = browser.find_element(By.XPATH, '//tr[35]//input[@value="1"]')
    browser.execute_script("arguments[0].click();", drive_or_not)

    license_car = browser.find_element(By.XPATH, '//*[@id="V1_CTRL217"]')
    browser.execute_script("arguments[0].value = '{}';".format(user.car_number), license_car)

    phone_number_teacher = browser.find_element(By.XPATH, '//*[@id="V1_CTRL379"]')
    browser.execute_script("arguments[0].value = '{}';".format(user.phone_teacher), phone_number_teacher)
    department_stu = browser.find_element(By.XPATH, '//*[@id="V1_CTRL377"]')

    browser.execute_script('''
    var daoyuanOption = document.createElement("option")
    daoyuanOption.value = "{}"
    daoyuanOption.text = "{}"
    console.log(daoyuanOption)
    arguments[0].appendChild(daoyuanOption)
    arguments[0].value = "{}"
    '''.format(user.id_department, user.department, user.id_department), department_stu)

    teacher_name = browser.find_element(By.XPATH, '//*[@id="V1_CTRL378"]')
    browser.execute_script('''
    var daoyuanOption = document.createElement("option")
    daoyuanOption.value = "{}"
    daoyuanOption.text = "{}"
    console.log(daoyuanOption)
    arguments[0].appendChild(daoyuanOption)
    arguments[0].value = "{}"
    '''.format(user.id_teacher, user.name_teacher, user.id_teacher), teacher_name)

    dorm_location = browser.find_element(By.XPATH, '//textarea[@id="V1_CTRL376"]')
    browser.execute_script("arguments[0].value = '{}';".format(user.dormitory), dorm_location)

    reason_for_enter = browser.find_element(By.XPATH, '//textarea[@id="V1_CTRL380"]')
    browser.execute_script("arguments[0].value ='开车入校，{}，{}';".format(user.name, user.card), reason_for_enter)


    apply_button = browser.find_element(By.XPATH, '//div[@class="commandC"]//a[@class="command_button_content"]//nobr')
    browser.execute_script("arguments[0].click();", apply_button)
    print('The appointment is done.')
    time.sleep(5)

def program_running_test():
    print( 'This program is running successfully... ')


if __name__ == '__main__':
    for user in user_info_list:
        apply_car(user)
