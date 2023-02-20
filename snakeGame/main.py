from turtle import Screen
import time
from Snake import Snake
from comida import Comida
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
comida = Comida()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.arriba, "Up")
screen.onkey(snake.abajo, "Down")
screen.onkey(snake.izquierda, "Left")
screen.onkey(snake.derecha, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.mover()

    # colision con comida
    if snake.head.distance(comida) < 15:
        comida.refrescar()
        scoreboard.refrescarScore()
        snake.extend()

    # colision con paredes
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 260 or snake.head.ycor() < -295:
        gameIsOn = False
        scoreboard.finJuego()

    # colision con cola
    for segment in snake.segmentos[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False
            scoreboard.finJuego()

screen.exitonclick()
