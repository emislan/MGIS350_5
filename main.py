#Emelia's
# NOTES:
# Install: https://flask.palletsprojects.com/en/2.0.x/installation/
# Quickstart: https://flask.palletsprojects.com/en/2.0.x/quickstart/
# To View: http://127.0.0.1:5000/
#


from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Hello, World!</p><hr><p>Welcome to Our Store!</p><hr><p>Here are our products</p><hr>"
