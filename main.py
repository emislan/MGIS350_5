#Emelia's
# NOTES:
# Install: https://flask.palletsprojects.com/en/2.0.x/installation/
# Quickstart: https://flask.palletsprojects.com/en/2.0.x/quickstart/
# To View: http://127.0.0.1:5000/
#


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p><hr><p>This is Emelia's Flask Page!</p><hr>"
