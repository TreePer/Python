myList = [11, 22, 23, 99, 81, 93, 35]

sum = 0 # 계산용 sum 변수 생성

for i in range(len(myList)) : # myList 길이 만큼 for문 반복
    sum += myList[i] # 차례대로 더함

print(sum) #결과 출력