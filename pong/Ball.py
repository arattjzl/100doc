from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.newBall()
        self.movX = 10
        self.movY = 10

    def newBall(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def mover(self):
        self.goto(self.xcor() + self.movX, self.ycor() + self.movY)

    def reboteY(self):
        self.movY *= -1

    def reboteX(self):
        self.movX *= -1

    def resetearPosicion(self):
        self.goto(0, 0)
        self.reboteX()
