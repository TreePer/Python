import turtle

t = turtle.Turtle() # 터틀 호출
t.shape("turtle")


def draw_square(size) :
    for i in range(size) : # size 만큼 반복
        t.forward(i * 10) # i x 10 만큼 이동
        t.left(90) # 왼쪽으로 90도 회전



draw_square(30) # 값을 넣어 함수 호출

turtle.mainloop()
turtle.bye()