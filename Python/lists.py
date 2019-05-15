my_list = [1,2,3]
new_list = [1,4.5,"hello",[3,4,5],2.34]
print(new_list)
print(new_list[1])
print(len(my_list))
my_list.extend(new_list)
print(my_list)
item = my_list.pop()
print(item)
print(my_list)
my_list.reverse()
print(my_list)