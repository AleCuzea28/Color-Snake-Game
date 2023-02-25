from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random
from tkinter import *


screen = Screen()
snake = Snake()
food =Food()
scoreboard = Scoreboard()

canvas = screen.getcanvas()

game_is_on = False


def screen_setup():
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("My snake game")
    screen.tracer(0)
    screen.colormode(255)


def controls():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    

def game_is_on_function():
    
    global game_is_on
    while  game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            new_color=(random.randint(20,255), random.randint(20,255), random.randint(20,255))
            for segment in snake.segments:
                segment.color(new_color)

        #Detect collision with wall
        if snake.is_collision_with_wall():
            scoreboard.reset()
            snake.reset()
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()    
                snake.reset()
                game_is_on = False
                scoreboard.game_over()
     

def button_click():
    global game_is_on
    game_is_on = True
    global button
    button.destroy()
    game_is_on_function()


screen_setup()
controls()  


button = Button(canvas.master,text = "START",command = button_click,height = 2,width = 10)
button.pack()
button.place(x=250, y=100)  # place the button anywhere on the screen
        

#screen.mainloop()
screen.exitonclick()