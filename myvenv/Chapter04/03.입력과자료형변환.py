# x = input("첫번째 숫자를 입력하세요>>>", )
# y = input("두번째 숫자를 입력하세요>>>", )

# print(type(x))

# #숫자형으로 변호나 int 함수를 사용하면 쇤다. : int(데이터)
# sum = int(x)+int(y)
# print("표준출력", sum)

# 태어난 연도를 가지고 현재 나이를 입력하세요.
import datetime
My_datetime = datetime.datetime.now()
x = input("태어난 연도를 입력하세요>>>")
age = My_datetime.year - int(x) + 1

print("현재 나이는",age," 세 입니다.")



