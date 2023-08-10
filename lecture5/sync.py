#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu)
print(menu,type(menu)) #class set 중괄호
menu = list(menu)
print(menu, type(menu)) #대괄호

menu = tuple(menu)
print(menu, type(menu)) #소괄호

menu = set(menu)
print(menu, type(menu))
