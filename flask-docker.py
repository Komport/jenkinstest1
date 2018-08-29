from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    for i in range(0,10000000):
        print(i)
    #return "Hello World! - IBO SUCKS :D"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
