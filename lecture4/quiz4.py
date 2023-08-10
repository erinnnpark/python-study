# from random import *
# # lst =[1,2,3,4,5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# # print(sample(lst,1)) #lst에서 1개를 샘플로 뽑겠다

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # list = set(list)

# # print(sample(list,1))

# # print(sample(list,3))



# # # 정민의 해답
# # winners = sample(list, 4)

# # shuffle(winners)

# # chicken_winner = winners.pop()
# # coffee_winner = winners

# # print("-- 당첨자 발표 --" + 
# #       f"\n치킨 당첨자 : {chicken_winner}" + 
# #       f"\n커피 당첨자 : {coffee_winner}" + 
# #         "\n-- 축하합니다 --")

from random import *
users = range(1,21) #1부터 20까지
# print(type(users)) 
users = list(users)
# print(type(users)) 
print(users)
shuffle(users)
print(users)
winners = sample(users,4) 
print("--당첨자 발표--")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--축하합니다--")


