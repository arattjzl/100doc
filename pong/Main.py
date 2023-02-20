import time
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

padDerecha = Paddle(350, 0)
padIzquierda = Paddle(-350, 0)
pelota = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(padDerecha.arriba, "Up")
screen.onkey(padDerecha.abajo, "Down")
screen.onkey(padIzquierda.arriba, "w")
screen.onkey(padIzquierda.abajo, "s")

gameOn = True
tiempo = 0.1
while gameOn:
    time.sleep(tiempo)
    screen.update()
    pelota.mover()

    # rebota en las paredes inferior y superior
    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.reboteY()

    # rebota con paddle
    if (pelota.distance(padDerecha) < 50 and pelota.xcor() > 310) or (pelota.distance(padIzquierda) < 50 and pelota.xcor() < -310):
        pelota.reboteX()
        tiempo *= 0.9

    # punto para izquierda
    if pelota.xcor() < -380:
        pelota.resetearPosicion()
        score.actualizarDerecho()
        screen.update()
        tiempo = 0.1
        time.sleep(1)

    # punto para derecha
    if pelota.xcor() > 380:
        pelota.resetearPosicion()
        score.actualizarIzquierdo()
        screen.update()
        tiempo = 0.1
        time.sleep(1)

screen.exitonclick()
