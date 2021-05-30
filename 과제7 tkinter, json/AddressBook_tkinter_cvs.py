from tkinter import *
import json

address_book = {}

try:
    with open("./addressData.json", "r")  as f:
        lines = json.load(f)
        address_book = lines

except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
    pass
except EOFError:
    pass

def search() :
    e1.focus_set()
    if (address_book.get(e1.get()) == None): # 키값(이름)이 존재하지 않을 경우
        t.insert(END, "저장되지 않은 이름입니다.")
    else:
        info = address_book.get(e1.get()) # 키값이 존재하면 딕셔너리의 밸류를 info에 넣음
        t.insert(END, e1.get() + "을 검색 했습니다\n")
        t.insert(END, e1.get() + "의 전화번호 :" + info[0] + " " + e1.get() + "의 주소 :" + info[1])
    e1.delete(0, END)

def add() :
    e1.focus_set()
    name = e1.get() # name에 넣어 키값으로 사용
    info = [e2.get(), e3.get()] # info에 값을 넣어 리스트 생성
    address_book[name] = info
    t.insert(END, e1.get() + "을 추가 했습니다\n")
    e1.delete(0, END)

def delete() :
    e1.focus_set()
    if (address_book.get(e1.get()) == None): # 키값(이름)이 존재하지 않을 경우
        t.insert(END, "저장되지 않은 이름입니다.")
    else:
        address_book.pop(e1.get()) # 존재할경우 삭제
        t.insert(END, e1.get() + "을 삭제 했습니다\n")
    e1.delete(0, END)

def output() :
    e1.focus_set()
    for key in sorted(address_book):
        info = address_book.get(key)
        t.insert(END, key + "의 전화번호 :" + info[0] + " " + key + "의 주소 :" + info[1])
    e1.delete(0, END)

def saveExit() :
    with open("./addressData.json", "w") as f:
        json.dump(address_book, f, ensure_ascii=False, indent=4)
        f.close()
    t.insert(END, "저장 & 종료\n")
    exit()

window = Tk()
window.title("친구관리")

# Label 객체 생성 및 배치
l1 = Label(window, text="이름", pady=5)
l1.grid(row=0, column=0, sticky=W)
l2 = Label(window, text="전화번호")
l2.grid(row=1, column=0, sticky=W, pady=5)
l3 = Label(window, text="주소")
l3.grid(row=2, column=0, sticky=W, pady=5)

# Entry 객체 생성 및 배치
e1 = Entry(window, bg="orange", width=26)
e2 = Entry(window, bg="orange", width=26)
e3 = Entry(window, bg="orange", width=26)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

# Button 들을 배치하기 위한 Frame 생성 및 배치, window가 부모임
bFrame = Frame(window, pady=5)
bFrame.grid(row=3, column=0, columnspan=2)
b1 = Button(bFrame, text='검색', width=6, command=search)
b1.grid(row=0, column=0, padx=2)
b2 = Button(bFrame, text='추가', width=6, command=add)
b2.grid(row=0, column=1, padx=2)
b3 = Button(bFrame, text='삭제', width=6, command=delete)
b3.grid(row=0, column=2, padx=2)
b4 = Button(bFrame, text='출력', width=6, command=output)
b4.grid(row=0, column=3, padx=2)
b5 = Button(bFrame, text='종료', width=6, command=saveExit)
b5.grid(row=0, column=4, padx=2)

# Text 객체 생성 및 배치
t = Listbox(window, bg="orange", height=12, width=33, border=0)
t.grid(row=4, column=0, columnspan=2, pady=2)

# Create scrollbar
scrollbar = Scrollbar(window, orient='vertical')
scrollbar.grid(row=4, column=2, sticky=N+S)
# Set scroll to listbox
t.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=t.yview)
# Bind select
# t.bind('<<ListboxSelect>>', select_item)

window.mainloop()