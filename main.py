from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

#Game screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

#Controls for the snake
screen.listen()
screen.onkey(snake.down, "s")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.update()

#Game start
gameIsOn = True
while gameIsOn:
    
    screen.update()
    time.sleep(0.08)
    snake.move()

    #Collision detector with food
    if snake.head.distance(food) < 15:
        food.changePos()
        snake.extend()
        score.addPoint()

    #Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameIsOn = False
        score.gameOver()

    #Collision with tail
    for segment in snake.tiles:

        if segment == snake.head:
            pass

        elif(snake.head.distance(segment) < 5):
            gameIsOn = False
            score.gameOver()


screen.exitonclick()