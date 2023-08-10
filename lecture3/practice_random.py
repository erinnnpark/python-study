
# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

from random import *
# print(random()) #0.0d이상 1.0 미만의 임의의 값 생성
# print(random()*10) #0.0이상 10.0 미만의 임의의 값 생성
# print(int(random()*10)) #0~10
# print(int(random()*10) + 1) #1~10
# print('''
# ''')
# print(int(random() * 45)+1) # 1~45이하의 임의의 값
# print(randrange(1,46))#1~46미만의 값 생성 
# print(randint(1,45)) #1부터 45이하의 값 생성(1,45포함)

#퀴즈

from random import *
# print( randint(int(random()*10)+4,28))
print('오프라인 스터디 모임 날짜는' + str(randint(int(random()*10)+4,28)) + '일로 선정되었습니다.')
date = randint(4,28)
print('오프라인 스터디 모임 날짜는' + str(date) + '일로 선정되었습니다.')

sentence = "It's really sot today."
index = sentence.index("a")
print(index)
index = sentence.index("s", index+1)
print(index)
print("Red Apple\rPine")





