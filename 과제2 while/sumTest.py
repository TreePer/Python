import random

i = 0
j = 0


while True :
    x = random.randint(1, 100) # 1~100 난수생성1
    y = random.randint(1, 100) # 1~100 난수생성2

    answer = int(input('{0} + {1} = '.format(x, y))) # 난수 x + y의 정답 입력

    flag = (answer == (x + y)) # 정답 확인

    print(flag) # 정답 결과 출력

    if (flag == True) : # 정답일시
        i += 1 # 정답갯수증가
        j += 1 # 문제갯수증가
    else : # 틀렸을시
        j += 1 # 문제갯수만 증가

    if (j == 5) :
        print('총 {} 문제중 {} 문제를 맞추어 {}점 입니다.' .format(j, i, (i * 10))) # 포맷을 이용해 문제갯수 정답갯수 점수 (정답갯수 * 10) 를 입력
        break