absent = [2, 5] # 결석
no_book = [7] 
for student in range(1,11) : #1부터 10까지 출석번호 -> 한명씩 반복하면서 책을 읽으라고
    if student in absent:
        continue #그 안에 있는 문장 실행하지 않고 다음 반복으로 진행하라는
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break #바로 반복문 탈출
    print("{0}, 책을 읽어봐".format(student))