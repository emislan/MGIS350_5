from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NewMouthpieceForm(FlaskForm):
    mpName = StringField('Mouthpiece name', validators=[DataRequired()])
    mpType = StringField('Mouthpiece type', validators=[DataRequired()])
    mpPicture = StringField('Mouthpiece picture (URL or filename)')
    mpPrice = StringField('Mouthpiece Price')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class NewCaseForm(FlaskForm):
    caseName = StringField('Phone Case name', validators=[DataRequired()])
    caseType = StringField('Phone Case type', validators=[DataRequired()])
    casePicture = StringField('Phone Case picture (URL or filename)')
    casePrice = StringField('Phone Case Price')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
