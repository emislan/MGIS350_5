from main import db


class Mouthpiece(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	mpName = db.Column(db.String(64),index=True)
	mpType = db.Column(db.String(64),index=True)
	mpPrice = db.Column(db.Float,index=True)
	mpPic = db.Column(db.String(256),index=True)
	
	def __repr__(self):
		return '<Mouthpiece named {}>'.format(self.mpName)
