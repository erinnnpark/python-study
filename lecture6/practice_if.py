# weather = "맑음"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("오늘은 준비물이 필요 없어요.")

# weather = input("오늘 날씨는 어때요? ") 
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("오늘은 준비물이 필요 없어요.")

temp = int(input("기온은 어때요?")) #input은 문자열로 받는데, 기온은 보통 숫자니까 int로 감싸줌
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0<= temp <10 :
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")