import arcade 
class Rocket_pong(arcade.Sprite) :
    def __init__(self , x,y,c,n):
        super().__init__()
        self.center_x= x
        self.center_y= y
        self.change_x=0
        self.change_y=0
        self.color= c
        self.width= 10
        self.height= 60
        self.speed= 3
        self.score= 0
        self.name = n

    def move(self ,game ,  ball):
        if ball.center_x > game.width// 2 :
            # self.change_y = ball.change_y 
            if self.center_y > ball.center_y :
                self.change_y = -1 
            if self.center_y < ball.center_y :
                self.change_y = 1

            self.center_y += self.change_y * self.speed 

            if self.center_y < 50 :
                self.center_y  = 50
            if self.center_y > game.height - 50 :
                self.center_y = game.height - 50 

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , color= self.color )