class Game():
    def __init__(self, choice_1, choice_2):
        self.choice_1 = choice_1
        self.choice_2 = choice_2
    
    def game_function(self):
   
        if self.choice_1 == self.choice_2:
            return f"Both players have chosen {self.choice_1}. Nobody wins!"
        elif self.choice_1 == "rock":
            if self.choice_2 == "scissors":
                return "Rock beats scissors! Player 1 Wins!"
            else:
                return "Paper beats rock! Player 2 Wins!"
        elif self.choice_1 == "paper":
            if self.choice_2 == "rock":
                return "Paper beats rock! Player 1 Wins!"
            else:
                return "Scissors beats paper! Player 2 Wins!"
        elif self.choice_1 == "scissors":
            if self.choice_2 == "paper":
                return "Scissors beats paper! Player 1 Wins!"
            else:
                return "Rock beats scissors! Player 2 Wins!"



