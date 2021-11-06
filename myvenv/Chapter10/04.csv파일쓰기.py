import csv
data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3 ,8],
    ["형돈", 5,32]
]

file = open("./myvenv/Chapter10/student.csv","w", newline="", encoding="utf-8-sig")
# ere윈도우 자동으로 CSV파일 만들때 한 줄 뛰음 그것 방지 newline
# utg-8-sig 윈도우에서만 설정 vs에서도 깨지지 않음
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()