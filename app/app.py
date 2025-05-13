# pip install Flask
from flask import Flask, render_template, request, redirect
#from app.config import Config

app = Flask(__name__)
#app.config.from_object(Config)

@app.route('/')
def home():
    # Her kan fx hentes data og sættes ind i html-koden
    return render_template('index.html')

@app.route('/q1/')
def q1():
    txt = "Har du nogen sinde spildt vand?"
    return render_template('q1.html', title=txt)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=5000)
