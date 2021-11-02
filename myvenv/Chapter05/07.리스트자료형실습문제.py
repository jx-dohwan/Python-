# 실습문제 5.2.1
# 다음은 패스트 고등학고 2학년 3반 1번부터 5번까지의 1분간 팔굽혀펴기 개수이다.
# 데이터는 리스트에 저장되어 있다.
# 각문항을 실행한 결과를 출력해보사 result = [3,40,12,63,52]

# result = [33,40,12,63,52]

# # 문항1 : 6번의 팔굽혀펴기 개수는 9개이다. 추가하기
# result.append(9)
# print(result)

# # 문항2 : 2번은 재측정하여 50개를 하였다. 변경하기
# result[1] = 50
# print(result)

# # 문항3: 3번부터 6번까지 데이터를 슬라이징하자
# print(result[2:6])

# # 문항4 : 모든 데이터를 오름차순으로 정렬하자
# result.sort()
# print(result)

# 실습문제 5.2.2
# 털걸이 평균 측정 프로그램을 만들어 보자
# 먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다
# 그리고 일주일간의 턱걸이 횟수를 입력받아 리스트에 저장한다
# 리스트에 저장된 데이터의 평균을 구해 출력한다.

num = []

one_day = int(input("1일차 털걸이 횟수 >>>"))
num.append(one_day)
# one two day 할 필요 없다. 어차피 덮어지니까 하나로 함녀 된다.
two_day = int(input("2일차 털걸이 횟수 >>>"))
num.append(two_day)

three_day = int(input("3일차 털걸이 횟수 >>>"))
num.append(three_day)

fore_day = int(input("4일차 털걸이 횟수 >>>"))
num.append(fore_day)

five_day = int(input("5일차 털걸이 횟수 >>>"))
num.append(five_day)

six_day = int(input("6일차 털걸이 횟수 >>>"))
num.append(six_day)

seven_day = int(input("7일차 털걸이 횟수 >>>"))
num.append(seven_day)

result_sum = sum(num)
avg = result_sum/len(num)
print("평균 턱걸이 횟수:", int(avg) )