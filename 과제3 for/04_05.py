num = int(input("정수를 입력하시오 : ")) # 정수 입력

for i in range (0, num + 1) : # 입력받은 num 만큼 반복하기위해 num + 1 을함
    for j in range (0, i) : # 1부터 1 ~ num 까지 순서대로 한줄씩 출력 하는 for문
        j += 1 # 1씩 증가
        print(j, end = '') # 한 줄씩 쓰기 위해 end 사용
    print() # 한 줄 띄우기