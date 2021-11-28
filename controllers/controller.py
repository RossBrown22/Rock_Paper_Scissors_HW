from flask import render_template
from app import app
from models.player import Player
from models.game import Game
import random

@app.route('/')
def index():
    return render_template("index.html", title="Rock, Paper, Scissors")

@app.route("/rock")
def rock():
    choice = ["rock", "paper", "scissors"]
    player_1 = Player("Player 1", "rock")
    player_2 = Player("Player 2", random.choice(choice))
    game = Game(player_1.choice, player_2.choice)
    results = game.game_function()
    return render_template("index.html", title="The Results", results=results)

@app.route("/paper")
def paper():
    choice = ["rock", "paper", "scissors"]
    player_1 = Player("Player 1", "paper")
    player_2 = Player("Player 2", random.choice(choice))
    game = Game(player_1.choice, player_2.choice)
    results = game.game_function()
    return render_template("index.html", title="The Results", results=results)

@app.route("/scissors")
def scissors():
    choice = ["rock", "paper", "scissors"]
    player_1 = Player("Player 1", "scissors")
    player_2 = Player("Player 2", random.choice(choice))
    game = Game(player_1.choice, player_2.choice)
    results = game.game_function()
    return render_template("index.html", title="The Results", results=results)



