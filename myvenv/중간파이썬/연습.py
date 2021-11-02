# - 주석 : 한줄을 주석처러

# - 변수 : 데이터를 저장하는 장소
s = "data"
print(s) # 파이썬은 다른 언어랑 다르게 변수를 선언하지는 않는다.

# - None 데이터 타입
s = None
print(s)

# - 데이터 타입 불 : 논리값
print(True == True)
print(False == True)
print(False == False)

# - 데이터 타입 : 정수와 실수
i = 5
f = 5.6
print(type(i))
print(type(f))


# - 데이터 타입 : 문자열
s = "data"
s1 = 'data'
s2 = """data"""
s3 = '''data'''

print(s)
print(s1)
print(s2)
print(s3)

# - 데이터 타입 : 인덱스
s = "data"
print(s[1])
print(s[-1])

# - 문자열 슬라이스
s = "data"
print(s[0:2])
print(s[1:])
print(s[:3])
print(s[:])

# - 데이터 탐색
s = "data"
print(s.index('d'))
print(s.index('dat'))
print(s.rindex('d')) # 오늘쪽부터 먼저 계산하여 오늘쪽에서 먼저 나오는 숫자의 인덱스 값을 출력한다.

# - 특정 문자열의 존재 체크
s = "data"
print("da" in s)
print("z" not in s)
print(s.startswith('a'))
print(s.endswith('d'))

# - 특정 문자열의 갯수
s = "data"
print(s.count("a"))

# - 특정 문자열 바꾸기
s = "data"
print(s.replace("a", "*"))
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())

# - 화이이트 스페이스 제거
s = " data "
print(s)
print(s.strip(), end='!\n')
print(s.lstrip(), end='!\n')
print(s.rstrip(), end='!\n')

# - 문자열 포멧팅
s = "나는 {}벌레 {}가 없네"
print(s.format("개똥", "친구"))

# - 인덱스 포멧팅
s = "나는 {0}벌레 {1}가 없네"
print(s.format("개똥","친구"))

# - 이름 포멧팅
s = "나는 {z}벌레 {z1}가 없네"
print(s.format(z="개똥",z1="친구"))

# - 숫자와 문자열 간 및 숫자간 변환
print(int(2.1))
print(float(3))
print(str(3))
print(int("3"))
print(round(4.6))
import math
print(math.floor(4.6))
print(math.ceil(4.6))

# - 숫자와 문자열을 연산
print(str(3)+"2")
print(int("5")+5)

# - 랜점 정수, 실수(참고)
import random
print(random.randrange(1,10))
print(random.random())

# - 날짜 시간 생성
import datetime

my_datetime = datetime.datetime.now()
print(my_datetime)
my_datetime = datetime.datetime(2021, 10, 12, 11, 50, 23, 111)
print(my_datetime)
my_datetime = datetime.datetime(2021,10,12,11,50,44)
print(my_datetime)
my_datetime = datetime.datetime(2021,10,12,11,50)
print(my_datetime)
my_datetime = datetime.datetime(2021,10,12,11)
print(my_datetime)
my_datetime = datetime.datetime(2021,10,12)
print(my_datetime)

# - 문자열을 날짜 시간 변환 : strptime
import datetime
s = "1997-04-06 01:42:02"
my_datetime = datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
print(my_datetime)

# - 날짜 시간 수정 : replace()
import datetime

my_datetime = datetime.datetime.now()
my_datetime = my_datetime.replace(year=1997, month=4, day=6, hour=2, minute=20, second=23, microsecond=232)
print(my_datetime)

# - 날짜시간을 문자열로 변환 : strftime()
my_datetime = datetime.datetime.now()
print(my_datetime.strftime('%Y-%m-%d'))
# - 날짜 더하기 : datedelta, relativedelta
import datetime

my_datetime = datetime.datetime.now()
new_datetime = my_datetime + datetime.timedelta(days=1)
new_datetime = my_datetime + datetime.timedelta(weeks=2)
new_datetime = my_datetime + datetime.timedelta(hours=2)

from dateutil.relativedelta import relativedelta
new_datetime = my_datetime + relativedelta(years=2)
new_datetime = my_datetime + relativedelta(months=2)
print(new_datetime)

############이 밑의 것은 외울 것은 없는 것 같다. 이해하고 적용할 문제이다.
# - 화면 출력

# - 산술 연산자

# - 대입 연산자

# - 비교 연산자 : True or False -> 동등비교, 대조비교, 대조비교와 동등비교

# - 논리 연산자 : and 또는 or

# - 조건문

# - 반복문