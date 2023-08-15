# week = range(1,51)
# for day in week:
#     report_file = open(str(day) + "주차.txt","w", encoding="utf8")
#     print("- "+ str(day)+"주차 주간보고-",file=report_file)
#     print("부서:",file=report_file)
#     print("이름:",file=report_file)
#     print("업무 요약:",file=report_file)
#     report_file.close()
    
for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding = "utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")

