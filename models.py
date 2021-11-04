from main import db


class Mouthpiece(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	mpname = db.Column(db.String(64),index=True)
	mptype = db.Column(db.String(64),index=True)
	mpprice = db.Column(db.Float,index=True)
	mppic = db.Column(db.String(256),index=True)
	
	def __repr__(self):
		return '<Pet named {}>'.format(self.petname)


