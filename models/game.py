class Game():
    def __init__(self, choice_1, choice_2):
        self.choice_1 = choice_1
        self.choice_2 = choice_2
    
    def game_function(self):
   
        if self.choice_1 == self.choice_2:
            return f"Nobody Wins! Both players have chosen {self.choice_1}!"
        elif self.choice_1 == "rock":
            if self.choice_2 == "scissors":
                return "You Win! Rock beats scissors!"
            else:
                return "The Computer Wins! Paper beats rock!"
        elif self.choice_1 == "paper":
            if self.choice_2 == "rock":
                return "You Win! Paper beats rock!"
            else:
                return "The Computer Wins! Scissors beats paper!"
        elif self.choice_1 == "scissors":
            if self.choice_2 == "paper":
                return "You Win! Scissors beats paper!"
            else:
                return "The Computer Wins! Rock beats scissors!"



