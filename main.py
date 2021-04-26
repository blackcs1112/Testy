from flask import Flask, request
from sqlalchemy.orm import create_session
import sqlite3
import random
from flask import Flask
from flask import request, url_for
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from data import db_session
import db
import sqlite3



app = Flask(__name__)
db_session.global_init("db/users.db")

log = ''
pas = ''
@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
@app.route('/vhh', methods=['POST', 'GET'])
def vhh():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="log" placeholder="Введите логин" name="log">
                                    <input type="password" class="form-control" id="pas" placeholder="Введите пароль" name="pas">
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        global log, pas
        log = request.form['log']
        pas = request.form['pas']
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <title>Пример формы</title>
                      </head>
                      <body>
                        <div>
                            <form class="login_form" method="post">
                                <input value="Перейти к решению" type="button" onclick="location.href='http://127.0.0.1:8080/re'" />
                            </form>
                        </div>
                      </body>
                    </html>'''




@app.route('/re', methods=['POST', 'GET'])
def forma_vopr():
    global log, pas
    g = 0
    d = []
    list_word = []
    list_ans = []
    con = sqlite3.connect('db/vopro.db')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM vopro""").fetchall()
    for el in result:
        g = el[0]
    while len(d) != 10:
        r = random.randint(1, int(g))
        print(g)
        if r not in d:
            d.append(r)
            con = sqlite3.connect('db/vopro.db')
            cur = con.cursor()
            result = cur.execute(f"""SELECT * FROM vopro 
                WHERE id = {r} """).fetchall()
            for el in result:
                list_word.append(el[1])
                list_ans.append(el[2])
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <title>Вопрос</title>
                      </head>
                      <body>
                        <h1>Вопросы</h1>
                        <div>
                            <form class="login_form" method="post">
                                <h8>{list_word[0]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_0" rows="1" name="about_0"></textarea>
                                <h8>{list_word[1]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_1" rows="1" name="about_1"></textarea>
                                <h8>{list_word[2]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_2" rows="1" name="about_2"></textarea>
                                <h8>{list_word[3]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_3" rows="1" name="about_3"></textarea>
                                <h8>{list_word[4]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_4" rows="1" name="about_4"></textarea>
                                <h8>{list_word[5]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_5" rows="1" name="about_5"></textarea>
                                <h8>{list_word[6]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_6" rows="1" name="about_6"></textarea>
                                <h8>{list_word[7]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_7" rows="1" name="about_7"></textarea>
                                <h8>{list_word[8]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_8" rows="1" name="about_8"></textarea>
                                <h8>{list_word[9]}</h8>
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about_9" rows="1" name="about_9"></textarea>
                                <button type="submit" class="btn btn-primary">ответить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        g = 0
        con = sqlite3.connect('db/vopro.db')
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM vopro""").fetchall()
        for el in result:
            g = el[0]
        g = int(g) + 1
        con = sqlite3.connect('db/users.db')
        cur = con.cursor()
        resultss = cur.execute(f"""SELECT * FROM users""").fetchall()
        tt = 0
        print(resultss)
        for el in resultss:
            if el[1] == str(log):
                print(log)
                if el[2] == str(pas):
                    tt = el[0]
                    break
            else:
                print('вас нет в базе')
        list_about = [request.form['about_0'], request.form['about_1'], request.form['about_2'],
                      request.form['about_3'], request.form['about_4'], request.form['about_5'],
                      request.form['about_6'], request.form['about_7'], request.form['about_8'],
                      request.form['about_9']]
        print(list_about)
        tr = 0
        fl = 0
        for i in range(0, 10):
            if list_about[i] == list_ans[i]:
                con = sqlite3.connect('db/users.db')
                cur = con.cursor()
                cur.execute(f"""UPDATE users SET correct_answer = correct_answer + 1
                WHERE id = {tt}""")
                con.commit()
                con.close()
                tr += 1
            else:
                con = sqlite3.connect('db/users.db')
                cur = con.cursor()
                cur.execute(f"""UPDATE users SET wrong_answer = wrong_answer + 1
                        WHERE id = {tt}""")
                con.commit()
                con.close()
                fl += 1
        return f'Верно {tr}'



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

