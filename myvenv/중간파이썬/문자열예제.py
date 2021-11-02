# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0], letters[2])

# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[4:])

# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[::2])

# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])

# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요
phone_number = "010-1111-2222"
new_phone_number = phone_number.replace("-"," ")
print(new_phone_number)

# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))


#이름: 김민수 나이: 10 이름: 이철희 나이: 13 포멧팅 사용
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : {} 나이 : {} ".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"

print(int(상장주식수.replace(",","")))

# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (7IFRS연결)"
print(분기[:7])

# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print(data.strip())

# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
s = "hello"
print(s.capitalize())

# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.


# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split("-"))

# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
cho = int(input("숫자입력"))

if cho % 2 == 0:
    print("짝수")
else:
    print("홀수")


# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
num = int(input("입력값 : "))
numPul = num + 20

if numPul > 255:
    print("출력값 : 255")
else:
    print("출력값 : ",numPul)

