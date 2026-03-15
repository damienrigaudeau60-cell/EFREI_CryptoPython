from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Génération de la clé de chiffrement et création de l'objet Fernet0
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/exercice1')
def exo1():
     return render_template('exercice1.html')

@app.route('/exercice2')
def exo2():
     return render_template('exercice2.html'
    app.run(debug=True)
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
