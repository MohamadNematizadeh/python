import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__ (self, w):
        super().__init__("img/12.png")
        self.center_x = w//2
        self.center_y = 57
        self.width  = 99
        self.height = 99
        self.speed = 8
    
class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("img/bullet2.png")
        self.center_x = random.randint(0,w)
        self.center_y = h+24
        self.angle = 180
        self.width  = 48
        self.height = 48
        self.speed = 4



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=300,title="Interstellar Geme_Mohammad 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture("img/SaharaAndromeda_Coy_6135-scaled.jpeg")
        self.me = Spaceship(self.width)
        self.doshman = Enemy(self.width , self.height)
  # برای نمایش
    def on_draw(self):
         arcade.start_render()
         arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
         self.me.draw()
         self.doshman.draw()

    def on_key_press(self, symbol:int, modifiers:int):
        print("yek dokme feshar dade shod") 

        if symbol ==97:#   سمت چپ
            self.me.center_x = self.me.center_x-self.me.speed
        elif symbol == 100 :# سمت راست
            self.me.center_x = self.me.center_x+self.me.speed

    def on_update(self, delta_time:float):
        self.doshman.center_y-= self.doshman.speed


window = Game()
arcade.run()



