# encoding=utf8  
import sys,csv
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):

    with open('links.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        quotes = []
        for row in csv_reader:
            quotes.append(row)
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template(
        'test.html',**locals())
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
