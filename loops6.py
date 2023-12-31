# # x=[1,2,3,4]
# # s='cmp'
# # y=[]
# # for i in x:
# #     y.append(s+str(i))
# # print(y)
#
#
# # data ='i am babashankar from nalgonda. where are you from'
# #
# # u= 0
# # for i in 'aeiou':
# #     out = data.count(i)
# #     u= u+out
# #     print(i,out)
# # print('no of vowels ',u )
# #
# # out = {}
# # for i in range(1,11):
# #     out[i]=i*i
# # print(out)
# #
# # x=[3456,23,128,235]
# # y=[2,3,5,4]
# # b=[]
# # z=[]
# # for i in y:
# #     b.append(str(i))
# #
# # for i in range(len(y)):
# #
# #     m=int(''.join(b))
# #     if m in x:
# #         print(m)
# #     b.pop()
#
#
#
# d1 = {'a': 100, 'b': 200,'c':300}
# d2 = {'a': 300, 'b': 200,'d':400}
# d3={}
# # for i in d1:
# #     if d1[i] == d2[i]:
# #         d3[i] =d1[i]+d2[i]
# # print(d3)
# t=list(d1)+list(d2)
# out = sorted(set(t),key=t.index)
# for i in out:
#     if i in d1:
#         if i in d2:
#             d3[i] =d1[i]+d2[i]
#         else:
#             d3[i]=d1[i]
#     else:
#         d3[i] = d2[i]
#
# print(d3)
#


