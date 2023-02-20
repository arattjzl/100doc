from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xPos, yPos):
        super().__init__()
        self.crearPaddle(xPos, yPos)

    def crearPaddle(self, xPos, yPos):
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(xPos, yPos)

    def arriba(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def abajo(self):
        self.goto(self.xcor(), self.ycor() - 20)