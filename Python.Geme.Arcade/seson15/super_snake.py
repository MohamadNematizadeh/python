import random
import arcade

class Poor (arcade.Sprite):
    def __init__(self,game):
        super().__init__("img/poop.jpg")
        self.width = 32
        self.height = 32
        self.center_x =random.randint(10,game.width-10)
        self.center_y =random.randint(10,game.height-10)
        self.change_x = 0
        self .change_y = 0
class Pear (arcade.Sprite):
    def __init__(self,game):
        super().__init__("img/pear.png")
        self.width = 32
        self.height = 32
        self.center_x =random.randint(10,game.width-10)
        self.center_y =random.randint(10,game.height-10)
        self.change_x = 0
        self .change_y = 0

class Appale(arcade.Sprite):
      def __init__(self,game):
        super().__init__("img/apple.png")
        self.width = 32
        self.height = 32
        self.center_x =random.randint(10,game.width-10)
        self.center_y =random.randint(10,game.height-10)
        self.change_x = 0
        self .change_y = 0

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x =  game.width//2 -10
        self.center_y = game.height//2 -10
        self.color1 = arcade.color.KHAKI
        self.color2 = arcade.color.BROWN
        self.change_x = 0
        self.change_y = 0
        self.speed =4
        self.score = 0
        self.body = []
        self.snake_score = 1

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color1)
        for part in self.body:
            arcade.draw_rectangle_filled(part['x'], part['y'],
                                         self.width, self.height,self.color2 )
    def move(self):
        self.body.append({'x':self.center_x,'y':self.center_y})
        if len(self.body)>self.score:
         self.body.pop(0)
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

    def eat(self,food):
        del food
        self.score+=1   
class Game(arcade.Window):
    def __init__(self ,width,height):
        super().__init__(width= 800, height= 600,title="Super Snake🐍")
        self.background_game = arcade.load_texture('img/6.png')
        self.flag = 0

        self.snake = Snake(self)
        self.food =  Appale(self)
        self.pear =  Pear(self)
        self.poor =  Poor(self)


    def on_draw(self): 
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height,self.background_game)
        self.snake.draw()
        self.food.draw()
        self.pear.draw()
        self.poor.draw()
        output = f"Score: {self.snake.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLUE, 20) 
        if self.snake.snake_score  <= 0 or self.snake.center_x < 0 or self.snake.center_x > width or self.snake.center_y < 0 or self.snake.center_y > height:
            arcade.draw_text('GAME OVER', width//2, height//2, arcade.color.RED, 5 * 5, width=width, align='left')
            arcade.exit()
        arcade.finish_render()

   

    def on_update(self, delta_time:float) :
        self.snake.move() 
        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)  
            self.food = Appale(self)
        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat(self.pear)  
            self.pear = Pear(self)
        if arcade.check_for_collision(self.snake, self.poor):
            self.snake.eat(self.poor)  
            self.poor = Poor(self)
     
 
           

    def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.UP :   
                self.snake.change_x = 0
                self.snake.change_y = 1
            elif symbol == arcade.key.DOWN:
                self.snake.change_x = 0
                self.snake.change_y = -1
            elif symbol == arcade.key.LEFT:
                self.snake.change_x = -1
                self.snake.change_y = 0
            elif symbol == arcade.key.RIGHT:
                self.snake.change_x = 1
                self.snake.change_y = 0     
width= 800
height= 600
if __name__ == "__main__":
    game = Game(width,height)
    arcade.run()