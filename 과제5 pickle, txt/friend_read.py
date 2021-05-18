def start():
    address_book = {}  # 공백 딕셔너리를 생성한다.

    def save_addr(name, number, add, email) : # 한줄씩 저장하는 함수 생성
        with open("./friendData.txt", "a") as f:
            address_book[name] = [number, add, email]
            line = name + ", " + number + ", " + add + ", " + email + "\n"
            f.write(line)
            f.close()

    try:
        with open("./friendData.txt", "r") as f:
            while True :
                line = f.readline().strip() # 한줄씩 불러옴

                if not line : # 불러올 라인이 없으면 멈춤
                    break

                value = line.split(", ") # value에 line을 리스트로 넣음
                key = value.pop(0) # value 의 첫번째 값을 key값으로 넣음

                address_book[key] = value # 딕셔너리에 삽입

            f.close()

    except FileNotFoundError as e:
        print('파일이 존재하지 않습니다..', e)

    while True:

        user = display_menu()
        if user == 1:
            name, number, add, email = get_contact()
            save_addr(name, number, add, email)
            print("등록되었습니다.")

        elif user == 2:  # 삭제
            name = input("삭제할 이름 입력 : ")
            address_book.pop(name)
            print(f'{name} 님이 삭제 되었습니다')

            with open("./friendData.txt", "w") as f:  # 삭제할시 딕셔너리의 데이터를 바로 덮어쓰기함
                for key, value in address_book.items() :
                    line = key + ", " + value[0] + ", " + value[1] + ", " + value[2] + "\n"
                    f.write(line)
                f.close()

        elif user == 3: # 검색
            key = input("검색할 이름 입력 : ")
            if address_book.get(key) is None:
                print("저장되지 않은 이름입니다.")
            else:
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0])
                print(key, "의 주소 :", info[1])
                print(key, "의 이메일 :", info[2])
        elif user == 4: # 출력
            for key in sorted(address_book):
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0], key, "의 주소 :", info[1], key, "의 이메일 :", info[2])
        else:  # 종료
                print("종료합니다.")
                break

def get_contact():
    name = input("이름 : ")
    number = input("전화번호 :")
    add = input("주소 : ")
    email = input("이메일 : ")
    return (name, number, add, email)


# 메뉴를 화면에 출력한다.
def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

# __main__은 프로그램의 시작점
if __name__ == '__main__':
    start()