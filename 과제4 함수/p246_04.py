def getGrade(score) :
    if score >= 90 : #
        return print("A입니다.")
    elif score >= 80 :
        return print("B입니다.")
    elif score >= 70 :
        return print("C입니다.")
    elif score >= 60 :
        return print("D입니다.")
    else :
        return print("F입니다.")

getGrade(int(input("점수를 입력하시오 : "))) # 값을 입력받아 함수 호출