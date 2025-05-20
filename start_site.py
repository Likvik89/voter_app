from flask import Flask, render_template, request, redirect
import sqlite3
from app.config import Config
from app.forms import Q1_Form

app = Flask(__name__)
db = 'questions.db'
app.config.from_object(Config)



@app.route('/')
def home():
    # Her kan fx hentes data og sættes ind i html-koden
    return render_template('index.html')



@app.route('/q1/', methods=['POST', 'GET'])
def q1():
    q1_form = Q1_Form()
    if q1_form.validate_on_submit():
        if request.form.get("ja"):
            print("ja")
        
        if request.form.get("nein"):
            print("noin")

        return redirect('/')
    return render_template('q1.html', q1_form = q1_form)



if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=5000)
