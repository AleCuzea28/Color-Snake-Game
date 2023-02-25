from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("arial", 20, "normal")
TOP_HEIGHT = 270

class Scoreboard(Turtle):

    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("remember_high_score.txt") as data:
            self.high_score = int(data.read())        
        self.create_scoreboard()
 

    def create_scoreboard(self):
        self.penup() 
        self.color('white')
        self.hideturtle()
        self.goto(x = 0, y = TOP_HEIGHT)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align = ALIGNMENT, font = FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("remember_high_score.txt", mode = 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()    


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)    


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()        

