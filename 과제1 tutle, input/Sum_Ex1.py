def plus(a, b):
    return a + b # 덧셈 함수
def minus(a, b):
    return a - b # 뺄셈 함수
def multi(a, b):
    return a * b # 곱셈 함수
def divi(a, b):
    return a // b # 나눗셈 함수

while True:
    a = input("a : ") # a값을 먼저 입력받음
    if a != 'q': # a가 q가 아닐시
        op = input('+, -, *, / : ') # 산술 연산자 입력
        b = input('b : ') # b값 입력
        if op == '+': # +를 입력했을경우
            res = plus(int(a), int(b)) # 덧셈 함수 실행
        elif op == '-': # -를 입력했을경우
            res = minus(int(a), int(b)) # 뺄셈 함수 실행
        elif op == '*': # *를 입력했을경우
            res = multi(int(a), int(b)) # 곱셈 함수 실행
        elif op == '/': # /를 입력했을경우
            res = divi(int(a), int(b)) # 나눗셈 함수 실행
        else : # 입력이 제대로 되지 않았을 경우
            print("input error") # 에러메시지
        print("result : ", res) # 계산 결과 표시
        print("------------------")
    else:
        print("good bye") # 종료 메시지
        exit(0)