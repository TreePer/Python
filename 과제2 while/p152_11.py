x = 0
y = 0

x = int(input("몸무게를 입력하시오 : ")) # 몸무게 입력
y = int(input("키를 입력하시오 : ")) # 키 입력

y = y * 0.01 # cm로 입력받은 키를 m로 변환

bmi = x / (y * y) # bmi는 체중(kg)을 키의제곱으로 나누어 구함

if bmi >= 30 : # 30 이상일때
    print("비만입니다")
elif bmi >=25 : # 25 이상일때
    print("과체중입니다")
elif bmi >= 20 : # 20 이상일때
    print("정상입니다")
else :
    print("저체중입니다")