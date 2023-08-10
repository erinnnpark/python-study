
# def std_weight(height, gender) :
#     height_m = height *0.01
#     if gender == "남자" :
#      print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, round(pow(height_m,2)*22,2)))
    
#     else : 
#      print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, round(pow(height_m,2)*21,2)))

# std_weight(175, "남자")

def std_weight(height, gender) : 
    if gender == "남자" :
        return height * height * 22
    else :
        return height * height * 21

height = 175 
gender = "남자"

weight = round(std_weight(height /100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
    
        