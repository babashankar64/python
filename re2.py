# data= 'google.com'
# b=[]
# for i in range(len(data)-1,-1,-1):
#     b.append(data[i])
# h=''.join(b)
# print(h)
# k=0
# data=['ab','abc','xyz','aba','1221']
# for i in data:
#     if len(i)>=3:
#         if i[0]==i[-1]:
#             k=k+1
# print(k)
# data= 'abbbbbbbbcbb'
# k=0
# d=[]
# for i in range(len(data)-1):
#
#     if data[i]!=data[i+1]:
#         k=1
#         print(data[i], k)
#         k=0
#     else:
#         k=k+1
#     print(data[i], k)
#
#
# print(d)



# data = 'abbbbbbbbcbb'
# k=0
# temp={}
# for i in range(len(data)):
#     if i in temp:
#         k=k+1
#         temp[data[i]]=k
#     else:
#         k=1
#         temp[data[i]] = k
# print(temp)
#
# n=8
# for i in range(n):
#     print(' '*(int(n)-i-1),end="")
#     print("*"*(i),end='')
#     print("*" * (i-1))
# for i in range(n-1,0,-1):
#     print(' ' * (int(n) - i - 1), end="")
#     print("*" * (i), end='')
#     print("*" * (i - 1))
#
#
P=15
S=P//2#7
for i in range(1,P,2):#1,3,5,7,9,11,13,15
    part1 = ' '*S#7
    part2= '*'*i#1
    print(part1+part2)
    S = S-1

S=0
for i in range(P, 0, -2):  # 1,3,5,7,9,11,13,15
    part1 = ' ' * S  # 7
    part2 = '*' * i  # 1
    print(part1 + part2)
    S = S + 1