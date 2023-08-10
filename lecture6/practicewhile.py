#while(조건) - 조건이 만족할 때까지 반복
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1 #부르는 횟수를 줄여나감
    if index == 0 :
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True :
        print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
        index += 1

        #무한루프 -> 종료하려면 컨트롤 C
        

