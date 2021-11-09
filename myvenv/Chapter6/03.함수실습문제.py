# 실습문제 6.1.2
# 다음은 세개의 정수를 인자로 받아, 합계와 평균을 출력해주는 함수이다. 함수를 호출한 결과로 표준 출력이 나오도록 함수를 정의해보자
# tip : docstring : 설명문
# tip : 문자열 포맷팅

def printSumAvg(x,y,z):
    """
    세가지 수의 합계, 균을 구하는 함수
    """
    sum = x + y + z
    avg = sum / 3
    print("합계 : {}  평균 {}".format(sum,avg))
    print(f"합계 : {sum}  평균 {avg}")

# 함수호출
printSumAvg(10,20,30)

# 표준출력
# 합계 : 60
# 평균 : 20

# 실습문제 6.1.3 매우 중요한 문제
# 로또에 당첨되서 퇴사를 하고 싶었던 김로또는 로또 예상번호 추츨 프로그램을
# 파이썬으로 작성하려고한다.
# 다음 조건에 따라 김로또의 프로그램을 완성해보자

# 1. 로또 번호 6개를 생성한다.
# 2. 로또 번호는 1~45까지의 랜덤한 ㅂㄴ호이다.
# 3. 5개의 숫자 모두 달라야 한다.
# 4. getRandomNumber()함수를 사용해서 구현한다. landom모듈dml sample함수는 사용하지 않는다
# 5. 반복분, 조건문, 리스트가 들어간다.

import random


def getRandomNumber():
    number=random.randint(1,45)
    return number
    
lotto_num = []

count = 0 # 현재 뽑은 숫자

while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num: 
        lotto_num.append(random_number)
        count += 1

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")
