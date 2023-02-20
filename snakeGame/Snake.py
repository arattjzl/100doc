from turtle import Turtle

POSICION_INCIO = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_MOVIMIENTO = 20
ARRIBA = 90
ABAJO = 270
IZQUIERA = 180
DERECHA = 0

class Snake:

    def __init__(self):
        self.segmentos = []
        self.crear_snake()
        self.head = self.segmentos[0]

    def crear_snake(self):
        for posicion in POSICION_INCIO:
            segmento = Turtle("square")
            segmento.color("white")
            segmento.penup()
            segmento.goto(posicion)
            self.segmentos.append(segmento)

    def mover(self):
        for seg in range(len(self.segmentos) - 1, 0, -1):
            self.segmentos[seg].goto(self.segmentos[seg - 1].xcor(), self.segmentos[seg - 1].ycor())
        self.head.forward(DISTANCIA_MOVIMIENTO)

    def arriba(self):
        if self.head.heading() != ABAJO:
            self.head.setheading(ARRIBA)

    def abajo(self):
        if self.head.heading() != ARRIBA:
            self.head.setheading(ABAJO)

    def izquierda(self):
        if self.head.heading() != DERECHA:
            self.head.setheading(IZQUIERA)

    def derecha(self):
        if self.head.heading() != IZQUIERA:
            self.head.setheading(DERECHA)
