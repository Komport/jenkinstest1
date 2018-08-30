from flask import Flask
from pyfiglet import Figlet
import os

app = Flask(__name__)

font = Figlet(font="colossal")

@app.route("/")
def index():
    return "Flask App!"
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
