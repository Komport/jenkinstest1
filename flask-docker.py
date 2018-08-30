from flask import Flask
from pyfiglet import Figlet
import os
app = Flask(__name__)
font = Figlet(font="starwars")
@app.route("/")
def hello_world():
    return "Hello World! - IBO SUCKS :D"
    message = os.getenv("MESSAGE", "no message specified")
    html_text = font.renderText(message)\
            .replace(" ","&nbsp;")\
            .replace(">","&gt;")\
            .replace("<","&lt;")\
            .replace("\n","<br>")
    return "<html><body style='font-family: mono;'>" + html_text + "</body></html>"
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
