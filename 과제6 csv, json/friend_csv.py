import csv

def main():
    address_book = {} # 공백 딕셔너리를 생성한다.

    # 저장용 함수
    def save_address() : # encoding - 'utf-8-sig' 로 utf 코드가 안나오게함
        with open("./addressData.csv", "w", encoding = 'utf-8-sig', newline = '') as f :

            wr = csv.writer(f)

            for k, v in address_book.items() : # v1, v2에 각각 address_book의 밸류값을 나눠서 저장함
                v1 = v[0]
                v2 = v[1]

            wr.writerow([k, v1, v2])

            f.close()

    try:
        with open("./addressData.csv", "r", encoding = 'utf-8-sig') as f :
            lines = csv.reader(f) # csv파일에서 한줄씩 읽어옴
            for line in lines:
                key = line.pop(0) # key 값을 pop해서 key와 value로 분리함
                address_book[key] = line # value 삽입

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