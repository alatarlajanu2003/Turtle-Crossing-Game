from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
START_POSITION = (-300, 300)
NUMBER_CARS = 20

class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create()

    def create(self):
        for _ in range(NUMBER_CARS):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            x = randint(START_POSITION[0], START_POSITION[1])
            y = randint(-250, 300)
            new_car.goto(x, y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)
            if car.xcor() < -315:
                y = randint(-250, 300)
                car.goto(310, y)

    def accelerate(self):
        self.speed += MOVE_INCREMENT

