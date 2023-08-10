#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])

print(cabinet.get(3))
#print(cabinet[5]) 이렇게 하면 프로그램 오류로 작동하지 않음
print(cabinet.get(5)) #이거는 none 반환
print(cabinet.get(5, "사용 가능")) #5가 없으면 뒤에 문구가 출력됨

print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3":"유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)

