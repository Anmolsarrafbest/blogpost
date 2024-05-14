
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import jinja2 as j

app=Flask(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database" 
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.model):
    __tablename__='user'
    user_id=db.Column(db.String,primary_key=True)
    username=db.Column(db.string,Unique=True)
    email=db.Column(db.string,Unique=True)
    passward=db.Column(db.string)
    