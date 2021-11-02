# 딕셔너리
# : ㅎ사전형태의 자료형

stock_a = {"삼성전자" : 82000, "LG전자" : 15000}

stock_b = {
    "삼성전자" : [82000, 15999, 43923],
    "LG전자" : (29999,12343,23331)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 4,
        "매수단가" : 81000
    }
}
print(stock_a)
print(stock_b)
print(stock_c)

# 딕셔너리 집근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 82000,
    "SK하이닉스" : 12000,
    "NAVER" : 370000,
    "카카오" : 133000
}

# items() : 키와 데이터 쌍
for item in stock_d.items():
    print(item)
    print(item[0])
    print(item[1])

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)
