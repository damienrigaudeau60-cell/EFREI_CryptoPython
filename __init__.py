from flask import Flask, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)

@app.route("/")
def hello_world():
    return render_template("site/index.html")
