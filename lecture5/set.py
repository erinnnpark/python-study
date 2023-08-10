#set (집합, 중복안되고 순서가 없음)
my_set = {1,2,3,3,3}
print(my_set) #중복된 부분은 안나옴 
java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합 (자바는 가능, 파이썬 모르는 개발자)
print(java-python)
print(java.difference(python))

#파이썬할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊었음
java.remove("김태호")
print(java)


