import arcade
from snake import Snake

class Pear(Snake):
    def __init__(self, game):
        super().__init__('img/pear.png', game)
        self.width = 60
        self.height = 45
        self.score = 2