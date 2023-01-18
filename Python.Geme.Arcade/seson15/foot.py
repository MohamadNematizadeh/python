import arcade
import random
class Food(arcade.Sprite):
    def __init__(self, w, h):
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)
