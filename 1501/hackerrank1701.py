inp_list1 = input().split(' ')
inp_list2 = input().split(' ')

inp2=[]
for i in inp_list1:

    for j in inp_list2:
        inp1 = []
        inp1.append(int(i))
        inp1.append(int(j))
        inp_tuple= tuple(inp1)
        print(inp_tuple, end=' ')
        inp2.append(inp_tuple)
print(inp2)
for i,j in inp2:
    k=int(i)
    l=int(j)


# out = ' '.join(inp2)
# print(out)
#



from itertools import combinations
inp = input().split(' ')
inp1 = inp[1]
inp2 = inp[0]
inp_list=[]
for i in inp2:
    inp_list.append(i)
sort_list=sorted(inp_list)
out_list=[]

for i in range(1,int(inp1)+1):
    for out in (list(combinations(sorted(inp_list),i))):
        print(''.join(out))
    # print(out)
    # out_list.append(out)
# for d in out_list:
#     print(d)
    # for j in d:
    #     # output = ''.join(list(j))
    #     print(j)
    #     pass
# for p in sort_list:
#     print(p)
# sort_lis = sort_list.copy()
# sort_list2 = sort_list.copy()
# for k in sort_list2:
#     sort_lis.remove(sort_lis[0])
#     for a in sort_lis:
#             print(k, end='')
#             print(a)
# for k in sort_list2:
#     sort_lis.remove(sort_lis[0])
#     for a in sort_lis:
#             print(k, end='')
#             print(a)

#     #     output = ''.join(list(d))
    # #     print(output)
    #     sort_list2 = out.copy()
    #     sort_list1 = out.copy()
        # for k in sort_list2:
        #     sort_list1.remove(sort_list1[0])
        #     for j in sort_list1:
        #         print(k, end='')
        #         print(j)
        #


# for p in sort_list:
#     print(p)
# sort_list2 = sort_list.copy()
# sort_list1=sort_list.copy()
#
# for k in sort_list2:
#     sort_list1.remove(sort_list1[0])
#     for j in sort_list1:
#         print(k,end='')
#         print(j)

#
# ls = [1,2,3,4]
# ls1=[1,2,3,4]
# for i in ls:
#     ls1.remove(ls1[0])
#     for j in ls1:
#         print(i,end='')
#         print(j)
# out=(list(permutations(sorted(inp_list),int(inp1))))

# print(out)
# for i in out:
#     output=''.join(list(i))
#     print(output)