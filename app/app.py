# pip install Flask
from flask import Flask, render_template, request, redirect
#from app.config import Config

import sqlite3

from forms import Q1_Form

app = Flask(__name__)

db = 'app\questions.db'
#app.config.from_object(Config)

@app.route('/')
def home():
    # Her kan fx hentes data og sættes ind i html-koden
    return render_template('index.html')

"""
@app.route('/q1/', methods=['POST', 'GET'])
def q1():
    q1_form = Q1_Form()
    if q1_form.validate_on_submit():
        if q1_form.valg.data:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            valg = q1_form.valg.data
            print(valg)
            cursor.execute('INSERT INTO driver(result) VALUES ('+valg+')')
            conn.commit()
            conn.close()
            return redirect('/')
    return render_template('q1.html', q1_form = q1_form)
"""


@app.route('/q1/', methods=['POST', 'GET'])
def q1():
    q1_form = Q1_Form()
    if q1_form.validate_on_submit():
        if request:
            pass

    return render_template('q1.html', q1_form = q1_form)


if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=5000)
