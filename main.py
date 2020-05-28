from flask import Flask, render_template, redirect, session
from kivy.app import App
from kivy.uix.widget import Widget

import gamestate



app = Flask(__name__)

@app.route('/')
def root():
	return render_template("root.html")

if __name__ == '__main__':
	lol = gamestate.GameState()
	lol.prout()
	app.run(host='0.0.0.0', port=8000)