from turtle import  Turtle
from random import randint

class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color('gold')
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed('fastest')
        self.move_around()

    # move food to random location on screen
    def move_around(self):
        self.goto((randint(-280, 280), randint(-280, 280)))
        
    