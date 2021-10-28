#Emelia's
#
#
#
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p><hr><p>This is Emelia's Flask Page!</p><hr>"
