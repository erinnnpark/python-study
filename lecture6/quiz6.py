

# from random import * 
# a = "O"

# for person in range(1,51) : 
#     time = randint(5,51)
#     if 5 <= time <= 15 : 
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(a,person, randint(5,51)))
#     else :
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(" ",person, randint(5,51)))

# print ("총 탑승 승객: {}분")

from random import * 
cnt = 0  #총 탑승 승객수
for i in range(1,51) :
    time = randrange(5,51)
    if 5<= time <= 15 :
        print("[0] {0}번째 손님 (소요시간: {1}분)".format(i, time))
        cnt += 1
    else :
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))
