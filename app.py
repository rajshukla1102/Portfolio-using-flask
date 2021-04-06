from flask import Flask, render_template, redirect, url_for, request
# from flask_mysqldb import MySQL
# import yaml
import pymongo
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)


url="mongodb+srv://<yourusername>:<yourpassword>@cluster0.eszou.mongodb.net/<yourdb>?retryWrites=true&w=majority"

cluster=MongoClient(url)
db=cluster["db"]
collection=db['test']



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
            print(email)
            if(not name or not email or not message):
                err="All form fields required..."
                title="Re-submit"
                return render_template('failedform.html',err=err,name=name,email=email,title=title)
            else:
                collection.insert_one({"name":name, "email":email, "message": message})
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