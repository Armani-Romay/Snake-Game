from turtle import Turtle

# a unit of the snake
class Segment:
    def __init__(self, initial_position) -> None:
        self.position = initial_position
        self.turtle = Turtle(shape='square')
        self.turtle.color('white')
        self.turtle.penup()
        self.turtle.goto(initial_position)
        self.direction = 'right'


    # return position
    def get_position(self):
        return self.position

    # move segment to desired coordinate
    def change_position(self, new_position):
        self.turtle.goto(new_position)
        self.position = new_position

# unit of snake that represents head
class Head(Segment):
    def __init__(self, initial_position) -> None:
        super().__init__(initial_position)
       


    # advanced one segment length (20px)
    def move_forward(self):
        self.turtle.forward(20)
        self.position = self.turtle.pos()

    # change direction left
    def turn_left(self):
        if self.direction != 'right':
            self.turtle.setheading(180)
            self.direction = 'left'
        

    # change direction right
    def turn_right(self):
        if self.direction != 'left':
            self.turtle.setheading(0)
            self.direction = 'right'


    def turn_up(self):
        if self.direction != 'down':
            self.turtle.setheading(90)
            self.direction = 'up'
    
    def turn_down(self):
        if self.direction != 'up':
            self.turtle.setheading(270)
            self.direction = 'down'
       

    # check how far an object is 
    def get_distance(self, coordinates):
        return self.turtle.distance(coordinates)
        

    # check if crashed with wall
    def collission_wall(self):
        return self.position[0] > 290 or self.position[0] < -290 or self.position[1] > 290 or self.position[1] < -290


class Snake:
    def __init__(self) -> None:
        self.head = Head((0, 0))
        self.segments = [self.head, Segment((-20, 0)), Segment((-40, 0))]
        self.previous_tail_coord = (-40, 0)


    # move entire snake forward
    def move_forward(self):

        self.previous_tail_coord = self.segments[-1].get_position()

        for i in range(len(self.segments)- 1, 0, -1):
            self.segments[i].change_position(self.segments[i - 1].get_position())
        self.head.move_forward()

    # change directiions left
    def turn_left(self):
        self.head.turn_left()
        
    def turn_right(self):
        self.head.turn_right()
        
    def turn_up(self):
        self.head.turn_up()

    def turn_down(self):
        self.head.turn_down()

    # make snake bodoy larger when a food is eaten
    def eat_food(self):
        self.segments.append(Segment(initial_position=self.previous_tail_coord))
    
    # check whether snake head touched food
    def detect_collission_food(self, food):
        if self.head.get_distance(food) <= 15:
            self.eat_food()
            return True
        return False

    
    # check whether snake head touched the body
    def detect_collission_self(self):
        for x in range(1, len(self.segments)):
            if self.head.get_distance(self.segments[x].get_position()) <= 10:
                return True
            return False

    # check whether snake touched screem edges
    def detect_collission_wall(self):
        return self.head.collission_wall()
    
    # make snake revert to initial size and position
    def reset(self): 
        for seg in self.segments: 
            seg.turtle.goto(100000,100000) 
        self.segments.clear() 
        self.head = Head((0,0)) 
        self.segments = [self.head, Segment((-20,0)), Segment((-40,0))]
        self.previous_tail_coord = (-40,0) 
