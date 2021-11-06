import pay_module

print(pay_module.version)

#함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("A102030", 13000,"2021-03-23")
print(pay_info.get_pay_info())
print(pay_module.__name__)