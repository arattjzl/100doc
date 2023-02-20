from turtle import Screen
import time
from Snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()
