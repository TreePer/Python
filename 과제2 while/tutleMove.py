import turtle




def turtleMoveLeft (tu, rad, move) : # 터틀이 왼쪽으로 움직이는 함수
    tu.left(rad)
    tu.forward(move)

def turtleMoveRight (tu, rad, move) : # 터틀이 오른쪽으로 움직이는 함수
    tu.right(rad)
    tu.forward(move)

t = turtle.Turtle() # 터틀 함수 선언
t.shape("turtle") # 터틀 모양
t.width(3) # 줄 굵기
t.shapesize(3, 3) # 터틀 크기

while True :
    command = input("명령을 입력하시오 (l = 왼쪽으로 이동, r = 오른쪽으로 이동, q = 종료) : ") # 왼쪽 오른쪽 종료 입력

    if command == 'q' : #종료 입력시
        print('종료') # 메시지 표시
        turtle.bye() # 터틀 종료
        break # while문 종료

    #종료 입력을 안했을때
    

    if command == 'l' : # l 입력했을때 왼쪽으로 움직이는 함수에 대입
        rad = int(input("각도를 입력하시오 : ")) # 각도 입력
        move = int(input("이동거리를 입력하시오 : ")) # 이동거리 입력

        turtleMoveLeft (t, rad, move) # 입력받은 값을 함수에 넣고 실행

    elif command == 'r' : # r 입력했을때 오른쪽으로 움직이는 함수에 대입
        rad = int(input("각도를 입력하시오 : ")) # 각도 입력
        move = int(input("이동거리를 입력하시오 : ")) # 이동거리 입력

        turtleMoveRight (t, rad, move) # 입력받은 값을 함수에 넣고 실행

    else :
        print('다시 입력하세요') # 지정된 키를 입력하지 않았을때
        continue