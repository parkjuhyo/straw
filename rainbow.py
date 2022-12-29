import turtle as t

t.Screen().bgcolor("lightblue") #뒷배경 색
t.Screen().screensize(500,500) #스크린사이즈지정
t.Screen().setworldcoordinates(-300,300,300,900) #사용자 정의 좌표
t.Screen().tracer(0,0) #.tracer(0)은 코드들이 실행되는 과정을 스크린창에 출력하지 않음

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius) #원의 색을 채움
    t.end_fill()

def cloud(radius, cloud_color="white"): #구름 만드는 코드 위치를 옮기며 구름 5개를 그리도록 함
                                        # radius로 하얀색 원을 여러개 그려 겹쳐지면 구름처럼 보이게 하였음
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

def rainbow(radius=200,interval=10): #처음 원의 크기를 200으로 지정/다음색의 원과의 간격은 10으로 지정
    roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'pink', 'violet'] #무지개를 구성하는 색깔

    for r_color in roygbiv:
        filled_circle(radius,r_color)
        radius -= interval

        # Move turtle a up by a little
        t.left(90)
        t.forward(interval)
        t.right(90)

t.penup()

t.goto(100,900) #구름의 좌표 지정
cloud(20) #구름 크기
t.goto(-50,850) #구름의 좌표 지정
cloud(30) #구름 크기
t.goto(50,600) #구름의 좌표 지정
cloud(50) #구름 크기
t.goto(200,500) #구름의 좌표 지정
cloud(5) #구름 크기

t.goto(0,0)
rainbow(300,10) #무지개 좌표 지정

t.goto(-200,500) #무지개를 그린후 무지개에 걸친 구름좌표지정
cloud(15) #구름 크기
t.goto(50,400) #구름의 좌표 지정
cloud(10) #구름 크기
t.goto(50,300) #구름의 좌표지정
cloud(10) #구름크기

t.Screen().update()#tracer함수를 쓸떄 같이 써주는 함수/ 결과만 보여줄 수 있다.
input()