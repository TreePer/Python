import random # 랜덤 모듈 호출
import turtle # 터틀 모듈 호출

t = turtle.Turtle() # 터틀 객체 생성
t.shape("turtle")

n = 0 # while문에 사용할 변수 n 초기화

while n < 10 : # 10번 반복
    x = random.randint(0, 100) # 원을 그릴 x 좌표값 0~100을 랜덤으로 생성
    y = random.randint(0, 100) # 원을 그릴 y 좌표값 0~100을 랜덤으로 생성
    size = random.randint(20, 100) # 원 사이즈 20~100을 랜덤으로 생성

    t.penup() # 좌표로 이동할땐 선 x
    t.goto(x, y) # 랜덤 좌표로 이동

    t.pendown() # 그리기 위해 펜 준비
    t.circle(size) # 원 그림
    n += 1 # 실행횟수 1회 증가




turtle.mainloop()
turtle.bye()