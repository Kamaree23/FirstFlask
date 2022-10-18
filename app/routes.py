from app import app
from flask import render_template

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/Top5')
def Top5():
    Fav = ['Junior H', 'Grupo Firme', 'Wiz Khalifa', 'Peso Pluma','Calibre 50']
    return render_template('Base.html', Fav_artists = Fav)
