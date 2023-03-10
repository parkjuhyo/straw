import turtle as t #터틀그래픽 오리랑 풍선
t.Screen().bgcolor("lightblue")
t.Screen().screensize(500,500)
t.Screen().setworldcoordinates(-300,300,300,900)
t.Screen().tracer(0,0)

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def cloud(radius, cloud_color="white"):
    filled_circle(radius,cloud_color)
    t.forward(radius)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)

def rainbow(radius=200,interval=10):
    roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    for r_color in roygbiv:
        filled_circle(radius,r_color)
        radius -= interval

        # Move turtle a up by a little
        t.left(90)
        t.forward(interval)
        t.right(90)

t.penup()

t.goto(100,900)
cloud(20)
t.goto(-50,850)
cloud(30)
t.goto(50,600)
cloud(50)
t.goto(200,500)
cloud(5)

t.goto(0,0)
rainbow(300,10)

t.goto(-200,500)
cloud(15)
t.goto(50,400)
cloud(10)
t.goto(50,300)
cloud(10)

t.Screen().update()



 

t.begin_fill()
t.shape("turtle")
t.color("yellow")
t.circle(50)
t.end_fill()
t.penup()
t.goto(30,90)
t.pendown()
t.begin_fill()
t.color("red")
for i in range(3):
    t.forward(20)
    t.right(180/ 3)
t.end_fill()
t.penup()
t.goto(-10,60)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(6)
t.end_fill()
t.penup()
t.goto(40,-100)
t.pendown()
t.begin_fill()
t.color("yellow")
t.right(90)
t.forward(110)
t.left(90)
t.forward(250)
t.left(90)
t.forward(110)
t.left(90)
t.forward(250)
t.end_fill()
t.penup()
t.goto(400,0)
t.pendown()
t.begin_fill()
t.color("pink")
t.circle(50)
t.end_fill()
t.right(85)
t.forward(300)
t.penup()
t.goto(500, 100)
t.pendown()
t.begin_fill()
t.color("green")
t.circle(100)
t.end_fill()
t.penup()
t.goto(600,6)
t.pendown()
t.pensize(3)
t.forward(300)
t.penup()
t.goto(100,200)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(60)
t.end_fill()
t.penup()
t.goto(150,150)
t.pendown()
t.forward(800)
input()
