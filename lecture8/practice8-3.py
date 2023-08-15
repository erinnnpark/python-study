#파일 입출력


# score_file = open("score.txt","w", encoding="utf8") #w=덮어쓰기 utf8은 한글 파일 읽을때!!
# print("수학:0",file=score_file)
# print("영어:50",file=score_file)
# score_file.close
# #score.file을 쓰기 목적으로 열어 수학/영어 점수를 쓰고 파일을 닫음 

# score_file = open("score.txt", "a",encoding="utf8") #a= 이미 존재하는 파일에 뒤에 계쏙 이어서 씀
# score_file.write("과학:80")
# score_file.write("\n코딩:100") #print는 기본적으로 줄바꿈 있는데 write는 없어서 \n
# score_file.close 

score_file = open("score.txt","r",encoding="utf8") #읽는 목적으로 염
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8") 
print(score_file.readline(),end="") #줄별로 읽기, 한줄읽고 커서는 다음줄로 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

#파일에 몇줄있는지 모를때
score_file = open("score.txt","r",encoding="utf8") 
while True: #무한루프
    line = score_file.readline()
    if not line: #line이 없으면
        break #반복문 탈출
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readline() #list형태로 저장
for line in lines:
    print(line, end="")

score_file.close()