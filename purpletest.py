from turtle import *
import turtle
from turtle import Screen, Turtle

color = (0.60160, 0, 0.99220)  # (154, 0, 254)
target = (0.86330, 0.47660, 0.31255)  # (221, 122, 80)
turtle.title("Python Guides")
tur = Screen()
tur.tracer(False)

width, height = tur.window_width(), tur.window_height()

deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]

turt = Turtle()
turt.color(color)

turt.penup()
turt.goto(-width/2, height/2)
turt.pendown()

direct = 1

for distance, y in enumerate(range(height//2, -height//2, -1)):

    turt.forward(width * direct)
    turt.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    turt.sety(y)

    direct *= -1

tur.tracer(True)
tur.exitonclick()

