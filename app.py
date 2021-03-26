from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)


ab=yaml.load(open('db.yaml'))
app.config['MYSQL_USER'] = ab['mysql_user']
app.config['MYSQL_PASSWORD'] = ab['mysql_password']
app.config['MYSQL_HOST'] = ab['mysql_host']
app.config['MYSQL_DB'] = ab['mysql_user']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql=MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method== 'POST':
        try:
            data=request.form
            name=data['name']
            email=data['email']
            message=data['message']
            if(not name or not email or not message):
                err="All form fields required..."
                title="Re-submit"
                return render_template('failedform.html',err=err,name=name,email=email,title=title)
            else:
                cur=mysql.connection.cursor()
                # cur.execute('''CREATE TABLE myRecords (name VARCHAR(50)  , email VARCHAR(50) , message VARCHAR(400)) ''')
                cur.execute("INSERT INTO myRecords (name,email,message) VALUES(%s,%s,%s)",(name,email,message))
                mysql.connection.commit()
                cur.close()
 
                mess="Thankyou!! I will surely work on your suggestion..."
                return render_template("end.html",mess=mess)
                
        except:
            mess="Didn't recieve any message...."
            return render_template("end.html",mess=mess)
    else:
        mess="Form not submitted Please fill it correctly..."
        return render_template("end.html",mess=mess)



if __name__ == '__main__':
    app.run(debug=True)