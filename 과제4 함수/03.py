import turtle

t = turtle.Turtle()
t.shape("turtle")

t.up()  # 그리기전 왼쪽으로 이동
t.goto(-300,0)
t.down()

def turtle_circle(radius, count) : # 함수 생성
    for i in range(count): # count 만큼 반복
        t.circle(radius) # radius 사이즈의 원을 그림
        t.penup()
        if i < count - 1 : # i가 count 보다 작을때 오른쪽으로 이동
            t.forward(radius * 2 + 20)
            t.pendown()
        else:
            t.pendown()

turtle_circle(200, 5) # 함수호출

turtle.mainloop()
turtle.bye()