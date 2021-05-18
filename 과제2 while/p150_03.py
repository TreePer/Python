word = input('알파벳을 입력하시오')

if word.lower() == 'c' : # lower()를 이용해 소문자로 변환해서 비교
    print('Circle')
elif word.lower() == 'r' :
    print('Rectangle')
elif word.lower() == 't' :
    print('Triangle')
else : # 일치하는 문자가 없을시 Unknown 표시
    print('Unknown')