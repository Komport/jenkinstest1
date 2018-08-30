from flask import Flask
from pyfiglet import Figlet
import os

app = Flask(__name__)

font = Figlet(font="colossal")

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/templates")
def hello(name):
    return render_template(
        'test.html',name=name)
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
