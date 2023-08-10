#지역 변수(함수내에서만 쓸 수 있음)와 전역 변수(모든 공간에서 부를 수 있는 변수)
gun = 10

def checkpoint(soldiers) :#경계근무
   global gun #전역 공간에 있는 gun 사용 
   gun = gun - soldiers
   print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) 
print("남은 총:{0}".format(gun))