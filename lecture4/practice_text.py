# sentence = '나는 소년입니다'
# print(sentence)
# sentence2="파이썬은 쉬워요"
# print(sentence2)
# sentence3 = ''' 나는 소년이고,
# 파이썬은 쉬워요
# '''
# print(sentence3)
jumin = "990120-1234567"
#슬라이싱
print('성별: ' + jumin[7])
print('연: ' + jumin[0:2]) #0부터 2직전까지(0,1)
print('월: '+jumin[2:4])#2,3
print('일: ' + jumin[4:6])
print('생년월일' + jumin[0:6]) #0부터 6직전까지
print('생년월일' + jumin[:6]) #처음부터 6직전까지
print('뒤 7자리' + jumin[7:14])
print('뒤 7자리' + jumin[7:]) #7부터 끝까지

print('뒤 7자리(뒤에부터)' + jumin[-7:]) #맨마지막이 -1






