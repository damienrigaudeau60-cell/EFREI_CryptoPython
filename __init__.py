from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Génération de la clé de chiffrement et création de l'objet Fernet0
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return index('index.html')

@app.route('templates/site/index.html')
def index():
     return render_template('index.html')

                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
