from collections import Counter
num_shoes = input()
shoe_sizes = input().split()
shoe_count = {}
for i in shoe_sizes:
    shoe_count[i] = shoe_sizes.count(i)
# shoe_count1 = Counter(shoe_sizes)
# shoe_count= dict(list(shoe_count1.items()))
num_customers = input()
money=0
for i in range(int(num_customers)):
    custo_info = input().split()
    for size,count in shoe_count.items():
        if custo_info[0] == size and count !=0:
            shoe_count[size]=count-1
            money=money+int(custo_info[1])
import re

#
# import re
# inp = '__com_'
# exp = '[A-Za-z0-9]+'
# out = re.search(exp,inp)
# out_num = out.group()
# print(out_num)
# out_list = []
# for i in out_num:
#     out_list.append(i)
# k=0
# out_list2 = []
# for j in range(0,len(out_list)-1):
#     if out_list[j] == out_list[j+1]:
#         k=out_list[j]
#         print(out_list[j])
# if not k:
#     print('-1')

#         k = k+1
#     else:
#         out_list2.append((k,out_list[j]))
#         k=1
# out_list2.append((k,out_list[j]))
# print((out_list2))

# 2. Write a program to find maximum number and second largest number withoutusing max
list1 = [10,20,30,55,22,41]
large = list1[0]
for i in list1:
    if i > large:
        large = i
print('larger number is',large)
list1.remove(large)
large2 = list1[0]
for i in list1:
    if i > large2:
        large2 =i
print('2nd largest number',large2)

# 3.
# str1 = "this is python"
# # Find the occurance of each character in above string
# for i in str1:
#     print(i,str1.count(i))


# for i in range(0,len(inp_list)-1):
#     if inp_list[i] == inp_list[i+1]:
#         count = count +1
#     else:
#         out_list.append((inp_list[i],count))
#         count = 1
# out_list.append((inp_list[i+1],count))
# for i,j in out_list:
#     print(i,j)

# 4. Reverse the string without using reverse

# name="hemalatha"
# for i in range(len(name)-1,-1,-1):
#     print(name[i],end='')
# out_list = []
# for i in name:
#     out_list.insert(0,i)
# print(''.join(out_list))

# dict1 = {"a":30,"b":40,"c":50}
# inp=input()
# for i,j in dict1.items():
#     if j== inp:
#         print(i)


# 8.
# list1 = [[1,2,3,4],[1,2,4],[45,68,79]]
# # convert list of list into single list
# list2=[]
# for i in list1:
#     list2.extend(i)
#
# print(list2)

# 9. Write a function to get no.of characters and numbers in given string
# Ex :
# str2 = "sasaidnid27381781"
#
# noc= 0
# non =0
# for i in str2:
#     if i.isdigit():
#         non=non+1
#     elif i.isalpha():
#         noc = noc +1
#     else:
#         break
# print(non)
# print(noc)



# 10. Write a program to match IP address using regex

exp = r'(^[0-1]?\d?\d|[2][1-5][1-5])\.([0-1]?\d?\d|[2][1-5][1-5])\.([0-1]?\d?\d|[2][1-5][1-5])\.([0-1]?\d?\d|[2][1-5][1-5])$'
inp = 'my ip address of 098 is 12.21.321 system is 0.107.1.126'

out1 = re.split("[ ]",inp)
for i in out1:
    i = i.strip()
    out = re.search(exp, i)
    if out:
        print(out.group())


# print(out1)
# out = re.search(exp,inp)
# print(out.group())













