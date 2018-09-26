import pymysql
from flask import Flask, render_template, request, session
app.secret_key = "monnie0708068740daizy"


app = Flask(__name__)


@app.route('/regi', methods=['GET', 'POST'])
def regi():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']

        con = pymysql.connect("localhost", "root", "", "exam")

        cursor = con.cursor()

        sql = "INSERT INTO `exam`(`firstname`,`lastname``username`,`password`) VALUES (%s,%s,%s,%s)"

        data = (firstname, lastname, username, password)

        cursor.execute(sql, data)
        con.commit()
        return render_template('regi.html')

    else:
        return render_template('regi.html')


@app.route('/login', methods=['GET', 'POST'])
def login(pymysql):
    if request.method == 'GET':

        username = request.form['username']
        password = request.form['password']

        if username == "" or password == "":
            return render_template('login.html')

        con = pymysql.connect("localhost", "root", "", "exam")
        cursor = con.cursor()

        sql = "SELECT * FROM  `exam` WHERE username = %s AND password =%s"

        data = (username, password)

        cursor.execute(sql, data)

        if cursor.rowcount == 0:
            return render_template('login.html', msg1="*Login failed!")
        elif cursor.rowcount == 1:
            results = cursor.fetchall()
            session['x'] = username
            return render_template('regi.html', results=results)
        else:
            return render_template('login.html')

    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug='true')
