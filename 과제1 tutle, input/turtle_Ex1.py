import turtle # 터틀 호출
import random # 랜덤 호출

myColors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange'] # 배열에 터틀로 그릴 색 추가

t = turtle.Turtle() # 터틀 객체 만들기

m = 0 # 글로벌 변수 생성

t.penup() # 그리지않기
t.goto(-300, 0) #(x : -300, y : 0) 좌표로 이동
t.pendown() # 다시그리기

def myTurtleMake (tur, move, radius, many): # 함수 생성 (터틀, 이동거리, 반지름, 원갯수)
    global m # 글로별 변수 호출

    m = move # 글로벌변수 m에 move값 대입

    for a in range(1, many): # many길이만큼 반복
        t.pencolor(myColors[random.randint(0, 5)]) # 랜덤으로 생성된 정수에 해당하는 변수 값으로 원 색깔 결정
        tur.circle(int(radius)) # radius값의 원 그리기
        tur.goto(-300 + (int(m)), 0) # move값만큼 오른쪽으로 이동
        m += move # move값 만큼 이동하기위해 계속 더해줌

    return tur

myTurtleMake(t, 30, 100, 10) # 함수에 값 넣어서 실행




turtle.mainloop()
turtle.bye()