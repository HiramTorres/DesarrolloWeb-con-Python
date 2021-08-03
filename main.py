from flask import Flask 
from flask import render_template


app = Flask(__name__)
@app.route('/')

def index():
    name = 'Hiram'
    lname = 'Torres'
    premium = True #La condición debe ser verdadera para que a la hora de renderizar se cree la etiqueta
    skills = ["Python", "Java", "C", "HTML"]
    return render_template("index.html",username=name,
                            lastname=lname,premium=premium,
                            skills = skills )

@app.route('/usuario/<username>')

def usuario(username):
    return 'Hola ' + username 



    

if __name__ == '__main__':
    app.run(debug=True,port=5000)