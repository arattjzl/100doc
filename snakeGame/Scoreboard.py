from turtle import Turtle

LINEAMIENTO = "center"
FUENTE = ("Courier", 20, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.nuevoScoreboard()
        self.hideturtle()

    def nuevoScoreboard(self):
        self.write(f"Score: {self.score}", False, LINEAMIENTO, FUENTE)

    def finJuego(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, LINEAMIENTO, FUENTE)

    def refrescarScore(self):
        self.score += 1
        self.clear()
        self.nuevoScoreboard()
