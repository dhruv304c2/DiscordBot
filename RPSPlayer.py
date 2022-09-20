class RPSPlayer:
    def __init__(self, name):
        self.name = name;
        self.win = 0;

    def win(self):
        self.win += 1;

    def move(self, move):
        self.move = move;
