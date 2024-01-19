# def test(*agrs,**kwargs):
     # print(kwargs)
# data = {'2':4,'5':8}
# data = {'ind':4, 'hyd':8}
# test(ind=4, hyd =8)

# def test(name='hi',number='00'):
#     print(name)
#     print(number)
# x='india'
# y=50
# test(number=y,name=x)
#
# def get_index(inp,value):
#     for i,j in inp.items():
#         if j==value:
#             return i
#
# inp_list = {'a':'b','c':'d','e':'f','g':'h',50:15}
# out = get_index(inp_list,15)
# print(out)
#
# data = ['a','b','c','a','a','d','e','f','g','h',50,15,'a','a']
# data_list = []
# for i in range(len(data)):
#     if data[i] == 'a':
#         data_list.append(i)
# def remove_all(data_list,value):
#     if (data_list[value] in data_list):
#         data.pop(data_list[value])
#         data_list.pop(value)
#
# remove_all(data_list,0)
# print(data)
# print(data_list)
#


dict1 = {"a":10,"b":31,"c":45}
# print sum of values

sum =0
for i,j in dict1.items():
    sum = sum+j
print(sum)

list1 = [10,100,200,100,99]
# 1. Find Largest number from above list
list_inp = list1[0]
for i in list1:
    if i>list_inp:
        list_inp = i
print(list_inp)
# 2. Find Second Largest mumber from list
list1.remove(list_inp)
list_inp2 = list1[0]
for i in list1:
    if i>list_inp2:
        list_inp2 = i
print(list_inp2)



# 3. Find smallest numbers from list
list_inp3 = list1[0]
for i in list1:
    if i<list_inp3:
        list_inp3 = i
print(list_inp3)

# 4. Print prime numbers from list
for number in list1:
    for i in range(2,number):
        if number % i ==0:
            break
    else:
        print(number,'is prime')


# 5. Find sum of even numbers
even_sum=0
odd_sum = 0
for i in list1:
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum = odd_sum + i
print(even_sum)
print(odd_sum)

# 6. Print sum of odd numbers

