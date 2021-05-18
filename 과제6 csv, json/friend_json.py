import json

def main():
    address_book = {} # 공백 딕셔너리를 생성한다.

    # 저장하는 함수
    def save_address() :
        with open("./addressData.json", "w") as f :

            json.dump(address_book, f, ensure_ascii=False, indent=4) # 아스키코드 변환 안함 ensure_ascii=False, 4줄 단위로 분리 indent=4  

            f.close()

    try:
        with open("./addressData.json", "r") as f :
            lines = json.load(f) # 하나씩 받아서 딕셔너리로 변환
            address_book = lines # address_book에 삽입

    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
        pass
    except EOFError :
        pass

    while True:
        user = display_menu()
        if user == 1:
            name, number, add = get_contact()
            info = [number, add]
            address_book[name] = info

        elif user == 2:
            name = input("삭제할 이름 입력 : ")
            address_book.pop(name)

        elif user == 3:
            key = input("검색할 이름 입력 : ")
            if(address_book.get(key) == None) :
                print("저장되지 않은 이름입니다.")
            else :
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0])
                print(key, "의 주소 :", info[1])

        elif user == 4:
            for key in sorted(address_book):
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0], key, "의 주소 :", info[1])

        else:
            save_address()
            break


def get_contact():
    name = input("이름 : ")
    number = input("전화번호 :")
    add = input("주소 : ")
    return (name, number, add)


# 메뉴를 화면에 출력한다.
def display_menu() :
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

if __name__ == "__main__" :
    main()