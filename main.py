
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import jinja2 as j
import random

def generate():
    return random.randint(10**15, 10**16 - 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3" 
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.String,primary_key=True,)
    username=db.Column(db.String, unique=True)
    email=db.Column(db.String, unique=True)
    passward=db.Column(db.String)

# class action(db.Model):
#    __tablename__='action'
@app.route("/log",methods=['GET'])
def log():
   return render_template("logg.html")    
@app.route("/",methods=['GET'])
def logging():
   return render_template("Home.html")

@app.route("/",methods=['POST'])
def logret():
   emailid=request.form['email_ID']
   password=request.form["pass"]
   user=request.form["username"]
   res=db.session.query(User).filter(User.email==emailid).first()
   if emailid==res:
      
      return render_template('Home.html',username="sign_in")
   else:
      user_id=generate()
      new_user=User(user_id=user_id,username=user,email=emailid,passward=password)
      db.session.add(new_user)
      db.session.commit()
      return render_template('Home.html',username=user)
    
# @app.route("/style/style.css",methods=["GET"]):
#    return {{url_for('s')}}   

if __name__ == '__main__':
  # Run the Flask app
  app.run(
    debug=True
  )    

import random

def generate():
    return random.randint(10**15, 10**16 - 1)

