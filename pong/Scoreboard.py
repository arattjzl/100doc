from turtle import Turtle

LINEAMIENTO = "center"
FUENTE = ("Courier", 30, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.puntosIzq = 0
        self.puntosDer = 0
        self.rapiedez = 0.1
        self.color("white")
        self.penup()
        self.goto(-100, 200)
        self.write(self.puntosIzq, False, LINEAMIENTO, FUENTE)
        self.goto(100, 200)
        self.write(self.puntosDer, False, LINEAMIENTO, FUENTE)
        self.hideturtle()

    def nuevoScoreboard(self):
        self.goto(-100, 200)
        self.write(self.puntosIzq, False, LINEAMIENTO, FUENTE)
        self.goto(100, 200)
        self.write(self.puntosDer, False, LINEAMIENTO, FUENTE)

    def finJuego(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, LINEAMIENTO, FUENTE)

    def actualizarIzquierdo(self):
        self.puntosIzq += 1
        self.clear()
        self.nuevoScoreboard()

    def actualizarDerecho(self):
        self.puntosDer += 1
        self.clear()
        self.nuevoScoreboard()

