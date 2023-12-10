#import methods 

class PlayerName:
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return f"{self.name}"
        
    player = input("Enter your name 'Name must include number and alphabets: ")


class Players:
    def __init__(self,playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo


class Statistics:
    def __init__(self, name, score, percentage, time, rank):
        self.name = name
        self.score = score
        self.percentage = percentage
        self.time = time
        self.rank = rank 