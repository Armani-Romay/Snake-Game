from turtle import Turtle 

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.score = 0 #initializing the starting score
        self.color("gold")
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.write_score()

    # method to write score
    def write_score(self):
       self.clear()
       self.write(f"Score: {self.score}", align="center", font=("Verdana", 25, "normal"))

    # increase the score by one and write the new score
    def increment_score(self):
        self.score += 1
        self.write_score()

    # game over screen
    def write_game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align="center", font=("Verdana", 69, "normal"))
        self.color("white")
        self.goto(0,-30)
        self.write("Press Space to Continue", align="Center", font=("Verdana", 18, "normal"))
        self.goto(0,265)
 
    # revert to initial scoreboard 
    def reset(self):
        self.score = 0 
        self.write_score() 