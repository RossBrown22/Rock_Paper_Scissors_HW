from flask import render_template
from app import app
from models.player import Player
from models.game import Game
import random

@app.route('/')
def index():
    return render_template("index.html", title="Rock, Paper, Scissors")

@app.route("/<choice_1>/<choice_2>")
def play(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1.choice, player_2.choice)
    results = game.game_function()
    return render_template("index.html", title="The Results", choice_1=choice_1, choice_2=choice_2, results=results)

