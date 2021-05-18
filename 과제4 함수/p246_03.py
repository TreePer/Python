def calc(x, y) :
    sum = x + y # 덧셈 계산
    minus = x - y # 뺄셈 계산
    mul = x * y # 곱셈 계산
    div = x / y # 나눗셈 계산
    return(print(sum, minus, mul, div,"이 반환되었습니다.")) # 계산 값을 반환함

a = int(input("첫 번째 정수를 입력하시오 : ")) # 첫번재 정수 입력
b = int(input("두 번째 정수를 입력하시오 : ")) # 두번째 정수 입력

calc(a, b) # 함수를 호출해 입력받은 정수를 대입

