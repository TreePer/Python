def display(count, *msg) : # 과제2 가변 길이 인수 선언
    for msgs in msg : # 입력받은 msg에서 하나씩 차례대로 출력
        for i in range(count) :#count 값을 받은만큼 반복
            print(msgs)


display(5, "안녕하세요", "반갑습니다")