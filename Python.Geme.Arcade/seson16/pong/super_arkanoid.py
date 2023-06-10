from random import randint
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 16
        self.height =16
        self.center_x=game.width 
        self.center_y =game.height
        self.change_x = 0
        self.change_y =1
        self.sped = 4

        def move(self):
         self.center_x += self.change_x*self.speed
         self.center_y += self.change_y*self.speed
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)   


class Brick(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("img/Ball.png")
        self.width = 58
        self.height =28
        self.center_x=x
        self.center_y =y
        self.change_x = 0
        self.change_y =1
        self.sped = 4
        self.color =  randint(0, 255) , randint(0, 255) , randint(0, 255)

class Game(arcade.Window):
    def __init__(self):
        super().__init__( width=500,height=600,title="Brick Breaker 2021")
        self.background = arcade.load_texture("img/back.png")
        self.bricks = []
        self.brickList = arcade.SpriteList()
        self.ball = Ball(self)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.brickList.draw()
        arcade.draw_rectangle_outline(self.width//2, self.height//2 - 15, self.width - 10, self.height-40,
            arcade.color.SONIC_SILVER, border_width=10)

        arcade.finish_render()   

    def on_update(self, delta_time):
        ...


game = Game()
arcade.run()






