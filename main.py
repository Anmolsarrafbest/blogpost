
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import jinja2 as j


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database" 
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.String,primary_key=True)
    username=db.Column(db.String, unique=True)
    email=db.Column(db.String, unique=True)
    passward=db.Column(db.String)

@app.route("/",methods=['GET'])
def logging():
   return render_template("logg.html")

@app.route("/",methods=['POST'])
def logret():
   emailid=request.form['email_ID']
   password=request.form["pass"]
   res=db.session.query(User).filter_by(User.email==emailid).first
   return render_template('anmol.html',emailid=emailid,password=password)

if __name__ == '__main__':
  # Run the Flask app
  app.run(
    debug=True
  )    