# list1 = [10,100,200,100,99,101,110]
#
# print([i for i in list1 if i%2 ==0])
#
#
list1 = [10,100,200,100,99,101,102]
# 1. Find Largest number from above list
max_list = list1[0]
secound_max = list1[1]
for i in range(len(list1)):
    if list1[i] > max_list:
        max_list = list1[i]
print(max_list)
list1.remove(max_list)
# print(secound_max)
secound_max = list1[1]
for i in range(len(list1)):
    if list1[i] > secound_max:
        secound_max = list1[i]
print(secound_max)
