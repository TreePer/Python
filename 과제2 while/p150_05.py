x, y, z = eval(input("3개의 정수를 입력하시오 : ")) #eval을 이용해서 3개의 정수를 입력받음

if x < y :
    if x < z :
        print("가장 작은 정수는 {} 입니다" .format(x)) # x가 y 보다 작고 z 보다도 작을때
    else :
        print("가장 작은 정수는 {} 입니다" .format(z)) # x가 y 보다 작고 z 보다 클때
elif x > y :
    if z > y :
        print("가장 작은 정수는 {} 입니다".format(y)) # y가 x보다 작고 z 보다도 작을때
    else :
        print("가장 작은 정수는 {} 입니다".format(z)) # y가 x보다 작고 z 보다 클때
else :
    print("같은 숫자가 있습니다.") # 같은 정수가 존재할때