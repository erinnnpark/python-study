print(1+1)
print(2+2)



print(2**3) #2^3
print(5%3) #5나누기 3의 나머지
print(5//3) #5나누기 3의 몫
print(10>3)
print(4>=7)
print(10<3)
print(3 == 3)
print(4 == 2)
print(3+4 == 7)
print(1 != 3) 
print(not(1 != 3))

print(3>0 and 3<5)
print(3>0 & 3<5)

print(3>0 or 3>5)
print((3>0) | (3>5))

print(4>3>2)
print(5>4>7)
#간단한 수식
print(2 + 3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number +2 #16 
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -=2
print(number)

number %=3
print(number)

#숫자처리함수
print(abs(-5))
print(pow(4,2)) # 4^2 = 16
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.99))
''' 

'''
from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

from random import *
print(random) #0.0~1.0 미만의 임의의 값
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10))

