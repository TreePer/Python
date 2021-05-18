number = 0 # 함수에서 값을 받아올 변수 선언

def checkEvenOdd(n) :

    global number # 함수에서 사용할수있게 글로벌 변수 선언

    n = number # 입력용 변수 선언

    while True :
        n = input("정수를 입력하시오 (종료 : '0000') : ") # 숫자 입력

        if (n == '0000') : # '0000' 이 입력되면 종료
            print("종료")
            break

        elif int(n) % 2 == 0 : # 문자열로 받아온 n을 int로 형변환 2로 나눈 나머지가 0일시 짝수
            print(f'{n}은 짝수')

        else :
            print(f'{n}은 홀수') # 2로 나눈 나머지가 0이 아닐시 홀수

checkEvenOdd(number)