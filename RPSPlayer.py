import os;
from dotenv import load_dotenv

load_dotenv()
rock = os.getenv('ROCK')
paper = os.getenv('PAPER')
scissors = os.getenv('SCISSORS')
class RPSPlayer:
    def __init__(self, name):
        self.name = name
        self.win = 0

    def win(self):
        self.win += 1

    def moveRock(self):
        self.move = rock

    def moveScissors(self):
        self.move = scissors

    def movePaper(self):
        self.move = paper
