from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='NVK'
)


@app.route('/')
def start():
    return render_template("home.html")

@app.route('/loginpg')
def homelog():
    return render_template('login.html')
@app.route('/homepg')
def homelog1():
    return render_template('home.html')

@app.route('/registerpg')
def loginpg():
    return render_template('register.html')

@app.route('/cartpg')
def cartpg():
    return render_template('cart.html')

@app.route('/aboutpg')
def aboutpg():
    return render_template('about.html')

@app.route('/contactpg')
def contactpg():
    return render_template('contact.html')

@app.route('/ayyappanpg')
def ayyappanpg():
    return render_template('ayyappan.html')

@app.route('/muruganpg')
def muruganpg():
    return render_template('/murugan.html')

@app.route('/omsakthipg')
def omsakthipg():
    return render_template('/omsakthi.html')

@app.route('/Buypg')
def Buypg():
    return render_template('/Buy.html')

@app.route('/view1pg')
def view1pg():
    return render_template('/view1.html')

@app.route('/view2pg')
def view2pg():
    return render_template('/view2.html')

@app.route('/view3pg')
def view3pg():
    return render_template('/view3.html')

@app.route('/view4pg')
def view4pg():
    return render_template('/view4.html')

@app.route('/view5pg')
def view5pg():
    return render_template('/view5.html')

@app.route('/view6pg')
def view6pg():
    return render_template('/view6.html')

@app.route('/view7pg')
def view7pg():
    return render_template('/view7.html')

@app.route('/view8pg')
def view8pg():
    return render_template('/view8.html')

@app.route('/view9pg')
def view9pg():
    return render_template('/view9.html')

@app.route('/view10pg')
def view10pg():
    return render_template('/view10.html')

@app.route('/view11pg')
def view11pg():
    return render_template('/view11.html')

@app.route('/view12pg')
def view12pg():
    return render_template('/view12.html')



@app.route('/reg', methods=['POST'])
def Submit():
    name = request.form['name']
    pswd = request.form['password']
    mail = request.form['email']
    date = request.form['dob']
    gen = request.form['Gender']
    pno = request.form['ph']
    q = 'insert into register (Name, Password, Email, DOB, Gender, Phone) values (%s, %s, %s, %s, %s, %s)'

    data = (name, pswd, mail, date, gen, pno)
    c = db.cursor()
    c.execute(q, data)
    db.commit()
    return render_template("login.html")

@app.route('/login',methods=['POST'])
def login():
    nme=request.form['name']
    psw=request.form['password']
    cu = db.cursor()
    q="select Name, Password from register where Name = %s"
    v=(nme,)
    cu.execute(q,v)
    user = cu.fetchone()
    if user:
        return render_template("home.html")
    else:
        return render_template('login.html')

if __name__ == '__main__':
     app.run()






