from flask import Flask, render_template, request
import mysql.connector
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置用于加密会话数据的密钥

# 配置数据库连接
db = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)

# 创建游标
cursor = db.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 在这里执行用户名和密码的验证逻辑
        # 验证通过时，可以将用户标记为已登录或创建一个会话
        
        # 示例逻辑：简单地比较用户名和密码是否匹配
        if username == 'admin' and password == 'password':
            # 登录成功，重定向到主页或其他受保护的页面
            return redirect('/home')
        else:
            # 登录失败，显示错误消息给用户
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    
    # GET请求时，渲染登录页面
    return render_template('login.html')

# 定义路由，处理表单提交
@app.route('/', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # 从表单中获取数据
        name = request.form['name']
        phone = request.form['phone']
        id_number = request.form['id_number']
        car_number = request.form['car_number']
        phone_teacher = request.form['phone_teacher']
        id_department = request.form['id_department']
        department = request.form['department']
        id_teacher = request.form['id_teacher']
        name_teacher = request.form['name_teacher']
        dormitory = request.form['dormitory']
        card = request.form['card']

        # 插入数据到数据库表
        sql = "INSERT INTO user_info (name, phone, id_number, car_number, phone_teacher, id_department, department, id_teacher, name_teacher, dormitory, card) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, phone, id_number, car_number, phone_teacher, id_department, department, id_teacher, name_teacher, dormitory, card)
        cursor.execute(sql, values)
        db.commit()

        return "数据已提交到数据库！"

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
