#표준 입출력

# print("Python","Java") #띄어쓰기 있음
# print("Python" + "Java") #띄어쓰기 없음
# print("Python", "Java", sep=",") #,를 대체하는 값 설정
# print("Python", "Java", "JavaScript", sep=" vs ") 
print("Python", "Java", sep=" vs ", end="?") #end : 문장의 끝부분을  ?로 바꿈
print("무엇이 더 재밌을까요?")  #end 때문에 5-6이 한줄로 나옴

import sys
print("Python", "Java", file=sys.stdout) #표준출력
print("Python", "Java", file=sys.stderr) #표전에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4),sep=":") #()숫자만큼 확보 후 왼쪽, 오른쪽 정렬

#은행 대기순번표 예시 
for number in range(1,21):
    print("대기번호: "+str(number).zfill(3)) #()크기만큼 공간 확보 후 값이 없는 빈공간에는 0으로 채움

#표준입력
answer = input("아무값이나 입력하세요: ") 
print("입력하신 값은 " + answer + "입니다.") #숫자, 문자 모두 잘 출력됨 - 다 문자열 형태로(스트링)으로 출력


