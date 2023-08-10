customer = "토르"
person = "Unknown"

while person != customer :   #이 조건에 만족할때까지 계속 프린트문을 반복! 토르가 와야 반복문 탈출 및 프로그램 종료
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")