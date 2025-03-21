from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']

        return f'Запрос отправлен методом POST. Имя пользователя {login}, пароль {password}'
    else:
        return render_template('auth.html')

@app.route("/main")
def main():
    data = ['user_1','user_2','user_3','user_4','user_5','user_6','user_7','user_8']

    return render_template('main.html', data = data)

@app.route("/main/<login>")
def mainWithParam(login):
    return f("{login}")
