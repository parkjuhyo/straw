import turtle
import random

t = turtle.Turtle()
turtle.bgcolor("black")
code_bag = ['red','green','blue','orange',"white","yellow","skyblue","purple","navy","indigo","pink"]
t.speed(0)
for x in range(100):
    t.up()
    t.goto(random.randint(-300,300), random.randint(-100,100))
    t.down()
    t.color(random.choice(code_bag)) 
    t.begin_fill()
    star_size = random.randint(10,30)
    for i in range(5):
        t.forward(star_size)
        t.left(144)
    t.end_fill()
input()