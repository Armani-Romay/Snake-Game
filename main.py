from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
from time import sleep

class GameController:
    
    def __init__(self) -> None:

        self.game_ended = False

        # Setup Screen
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.tracer(0)

        # Initialize instance of game objects
        self.scoreboard = Scoreboard()
        self.snake = Snake()
        self.food = Food()
        
        # add screen listeners
        self.screen.listen()
        self.screen.onkeypress(self.snake.turn_up, 'Up')
        self.screen.onkeypress(self.snake.turn_down, "Down")
        self.screen.onkeypress(self.snake.turn_left, 'Left')
        self.screen.onkeypress(self.snake.turn_right, 'Right')

        # start main loop
        self.game_loop()

        self.screen.exitonclick()

    # check whether snake head has touched food, if so eat it and move food
    def detect_collision_food(self):
        if self.snake.detect_collission_food(self.food):
            self.food.move_around()
            self.scoreboard.increment_score()

    # check for game over conditions and display game over screen
    def game_over(self):
        if self.snake.detect_collission_wall() or self.snake.detect_collission_self():
            self.game_ended = True
            self.screen.onkey(fun=self.reset_game, key="space") 
            self.scoreboard.write_game_over() 

    # reset the game
    def reset_game(self): 
            self.scoreboard.reset() 
            self.snake.reset() 
            self.screen.onkey(fun=None, key="space") 
            self.game_ended = False 
            self.game_loop()

    # main game looop, make snake go forward, update screen and check for collisioons with good and game over
    def game_loop(self):
        while not self.game_ended:
            self.snake.move_forward()
            sleep(0.1)
            self.screen.update()
            self.detect_collision_food()
            self.game_over()

GameController()
