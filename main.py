#Emelia's
# NOTES:
# Install: https://flask.palletsprojects.com/en/2.0.x/installation/
# Quickstart: https://flask.palletsprojects.com/en/2.0.x/quickstart/
# To View: http://127.0.0.1:5000/
#
#Zachary's Notes
# to establish the 2 classes and create a few examples of each class (similar to perotti's examplew in class)

#create models.py -- create class def of mps

from flask import Flask, render_template,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import NewCaseForm, NewMouthpieceForm
from config import Config

#Irrelevant
""" class Mouthpiece:
	def __init__(self,id,name,type,price,pic):
		self.id = id
		self.name = name
		self.type = type
		self.price = price
		self.pic = pic   
    
class PhoneCase:
	def __init__(self,id,name,type,price,pic):
		self.id = id
		self.name = name
		self.type = type
		self.price = price
		self.pic = pic """

""" Mouthpiecelist = []
p = Mouthpiece(0,"Frank Kaspar ", "Bb Soprano",650,"fluffy.jpg")
p2 = Mouthpiece(1,"Woodwind Company", "Bb Soprano", 120.00, "rover.jpg")
p3 = Mouthpiece(2,"Block Meliphone", "Eb Soprano",500,"cod.jpg")

PhoneCaseList = []
p = PhoneCase(0,"Frank Kaspar ", "Bb Soprano",650,"fluffy.jpg")
p2 = PhoneCase(1,"Woodwind Company" , "Bb Soprano", 120.00, "rover.jpg")
p3 = PhoneCase(2,"Block Meliphone", "Eb Soprano",500,"cod.jpg") """

# end of irrelevance

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import *

@app.route("/")
def welcome():
    return "<p>Hello, World!</p><hr><p>Welcome to Our Store!</p><hr><p>Here are our products</p><hr>"

# mouthpiece not defined -- issue

@app.route("/listmouthpieces")
def mplist():
	mouthpieces = Mouthpiece.query.all()
	return render_template("list.html",mouthpieces=mouthpieces)


@app.route("/detail/<int:pickamouthpiece>")
def detail(pickamouthpiece):
	mouthpiece = Mouthpiece.query.get(pickamouthpiece)
	return render_template("detail.html",mouthpiece=mouthpiece)

@app.route("/addmouthpiece",methods=['GET','POST'])
def addpet():
	addform = NewMouthpieceForm()
	if addform.validate_on_submit():
		flash('Adding pet {}, which is a...{}'.format(
			addform.mpName.data, addform.mpType.data))
		#nextpetid = len(petlist)
		p =Mouthpiece(mpName=addform.mpName.data,mpType=addform.mpType.data,mpPrice=addform.mpPrice.data,mppic=addform.mpPicture.data)
		db.session.add(p)
		db.session.commit()
		return redirect('/')
	return render_template("addMouthpiece.html",title='Add A Mouthpiece!',form=addform)


# IT ISNT LIKING HAVING 2 PRODUCTS (2 of each of the following types of code)

# @app.route("/listcases")
# def caselist():
# 	pets = PhoneCase.query.all()
# 	return render_template("list.html",case=case)

# @app.route("/detail/<int:pickacase>")
# def detail(pickacase):
# 	case = PhoneCase.query.get(pickacase)
# 	return render_template("detail.html",case=case)

if __name__ == "__main__":
	app.run()
