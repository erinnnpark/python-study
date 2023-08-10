#튜플: 내용 변경 및 추가 불가 (변경 안되는 목록 사용)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"

print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)