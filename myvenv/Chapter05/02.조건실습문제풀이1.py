# 실습문제 5.1.1
#  회사를 그만두게된 유진이는 유튜브를 시작하게 되었다. 
# 그리고, 유튜브를 통해 수익창출을 하려고 한다.
# 프로그램 사용자로부터 현재 구독자 수를 입력 받으면,
# 수익창충이 가능한지 불가능한지 알려주는 프로그램을 작성해보자
# 단, 수익창출은 구독자 1000명이상일 경우 가능하다.

# x = input("현재 구독자수를 입력하세요>>>")

# if int(x) >= 1000 :
#     print("수익 창출이 가능합니다.")
# else:
#     print("수익 창출이 불가능 합니다.!")


# 실습문제 5.1.2
# 윤행이는 평소 휴대푠을 너무 많이 사용해 공부시간을 다 빼앗기고 있었다.
# 이렇게 가면 얼마 남지 않는 기말고사를 망칠 게 뻔했다.
# 윤행이가 공부시간을 다 채울 경우에만 휴대폰을 사용할 수 있도록 프로그램을 만들어 주자
# 10시간 이상 : 휴대폰 잠금 해제, 5시간 이상 : 30분 사용가능 , 나머지 불가능

# study_time = int(input("공부시간을 입력하세요>>>"))

# if study_time >= 10 :
#     print("휴대폰 잠금이 해제됩니다.")
# elif study_time >= 5 :
#     print("휴대폰을 30분간 사용가능 합니다.")
# else:
#     print("휴대폰 사용이 불가능합니다.")

# 실습문제 5.1.3
# 현동이는 강의를 8시간 들으니, 배가 너무 고파 저녁을 먹리고 했다.
# 현동이가 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력해주는 프로그램
# 조건) 20000원 이상 : 치킨, 10000원이상 : 떡볶이, 2000원 이상 : 편의점 김밥

# my_money = int(input("현재 가짐 금액을 입력>>>"))

# if my_money >= 20000:
#     print("오늘 저녁은 뿌링클 및 사이드")
# elif my_money >= 10000:
#     print("오늘 저녁은 로제 떡볶이")
# elif my_money >= 2000:
#     print("오늘 저녁은 편의점 김밥ㅠㅠ")


# 실습문제 5.1.4
# 프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다.
# 세 과목의 평균 점수가 80점 이상이면 합격이다.
# 그런데 점수에 따라 합격 불합격이 정해지는 프로그램에 오류가 발행했다.
# 80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해보자
# 단)0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못입력하였습니다"를 출력하자

korean_score = int(input("국어 >>>"))
math_score = int(input("수학 >>>"))
english_score = int(input("영어 >>>"))

# 방법 1
average_score = (english_score+math_score+korean_score)/3

if average_score < 0 or average_score > 100:
    print("잘90못 입력했습니다.")
elif average_score >= 80:
    print("불합격")
else:
    print("합격")

# 방법 2
if 0 <= korean_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
    if average_score >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")

# 방법 3

if 0 > korean_score > 100 and 0 > math_score > 100 and 0 > english_score > 100:
    print("잘못 입력하였습니다.")
elif average_score >= 80:
    print("불합격")
else:
    print("합격")