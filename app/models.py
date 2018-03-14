from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:zszl15143121@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=True

db=SQLAlchemy(app)

#会员
class User(db.Model):
    __tablename__="user"
    id=db.column(db.Integer,primary_key=True)#编号
    name=db.Column(db.String(100),unique=True)#昵称
    pwd=db.Column(db.String(100))#密码
    email = db.Column(db.String(100), unique=True)#邮箱
    phone = db.Column(db.String(100), unique=True)#手机号
    info = db.Column(db.Text)#简介
    face=db.Column(db.String(255),unique=True)#头像
    addtime=db.Column(db.DateTime,index=True,default=datetime.UtcNow)#注册时间
    uuid=db.Column(db.String(255),unique=True)#标识符

    userlog=db.relationship('userlog',backref='user')
    def __repr__(self):
        return "<User %r>" %self.name

#会员登陆日志
class Userlog(db.Model):
    __tablename__="userlog"
    id=db.Column(db.Integer,primary_key=True)#编号
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))#会员id
    ip=db.Column(db.String(100))#登陆ip
    addtime=db.Column(db.DateTime,index=True,default=datetime.utcnow)#加上索引

    def __repr__(self):
        return "<Userlog %r>" %self.id

    #标签
    class tag(db.Model):
        __tablename__="tag"
        id=db.Column(db.Integer,primary_key=True)#编号
        name=db.Column(db.String(100),unique=True)#标题
        addtime=db.Column(db.DateTime, index=True, default=datetime.utcnow)#添加时间

        def __repr__(self):
            return "<Tag %r>" % self.name