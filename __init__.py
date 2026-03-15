from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)

@app.route("/")
def index():
    return render_template("templates/site/index.html")

if __name__ == "__main__":
    app.run()
