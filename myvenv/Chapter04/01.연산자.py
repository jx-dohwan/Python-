# 1. 대입 연산자
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산
x = 5
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # 몫
print(x%y) # 나머지
print(x**y) # 제곱

# - 문자열 연산
tag1 = "#내거하지"
tag2 = "#오늘부터1일"
tag3 = "#여친생김"

tag = tag1+ tag2+tag3
print(tag)

message = "나는 나고 너는 너다.\n" * 5
print(message)

#  복합할당연산자
level = 10 # 레벨 1증가
level += 1 # level = level + 1

health = 2000 #력이 300감소
health -= 300 # health = health - 300

attack = 300 # 공격력 1.5배 증가
attack *= 1.5 # attack = attack * 1.5

speed = 450 #이동속도 50% 감소
speed /= 2 # speed = speed / 2

print(level, health, attack, speed)