import random
from turtle import Turtle


class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fast")
        self.goto(random.randint(-270, 270), random.randint(-270, 250))
        self.refrescar()

    def refrescar(self):
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
