# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름:{0}\t나이:{1}\t".format(name, age),end =" ") #end를 쓰고 스페이스하면, 커서가 엔터안 된 상태에서 끝남(아랫줄이랑 이어서 한줄로 표기됨)
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language) : #가변인자 - 서로 다른 개수의 값을 넣어줄 때 사용
    print("이름:{0}\t나이:{1}\t".format(name, age),end =" ") 
    for lang in language:
        print(lang, end = " ")
    print()


profile("유재석", 20, "Python", "Java", "C","C++", "C#","Javascript")
profile("김태호", 25, "Kotlin","Swift")

