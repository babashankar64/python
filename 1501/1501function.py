# def common(a,b):
#     global c
#     c=[]
#     for i in a:
#         if i in b:
#             c.append(i)
#
#     print(locals())
# # x=[10,20]
# # y=[20,30,40]
# x=['india','uk','usa','aus']
# y=['hyd','nal','india','uk']
# common(x,y)
# print(c)
# def common(a,b):
#     global c
#     c=[]
#     for i in a:
#         if i in b:
#             c.append(i)
#     return c
#
#
# x=['india','uk','usa','aus']
# y=['hyd','nal','india','uk']
# a,b=common(x,y)
# print(a,b)
#
# s = '1 w 2 r 3g'
# inp = s.split(' ')
# count=1
# out_list=[]
# for i  in inp:
#     if not i.isdigit():
#         out=i.title()
#         out_list.append(out)
#         count=count+1
#         print(out)
#     else:
#         out_list.append(i)
# ou=' '.join(out_list)
# print(ou)

# for i  in inp:
#     if not i.isdigit():
#         out=i.title()
#         out_list.append(out)
#         count=count+1
#         print(out)
#     else:
#         out_list.append(i)
# ou=' '.join(out_list)
# print(ou)
# import re
#
# inp1 = s.split(' ')
# out_list=[]
# exp = r"\s+?[A-z]+\s+?"
# inp2 = re.findall(exp,s)
# inp=[]
# for i in inp2:
#     inp.append(i.strip())
# for i in inp1:
#     for j in inp:
#         if i==j:
#             out=j.title()
#             out_list.append(out)
#             break
#         else:
#             if i not in out_list and i not in inp:
#                 out_list.append(i)
# ou=' '.join(out_list)
s ='baba shan'
if not s.isdigit():
        return s.title()
    else:
        inp1 = s.split(' ')
        out_list=[]
        exp = r"\s+?[A-z]+\s+?"
        inp2 = re.findall(exp,s)
        inp=[]
        for i in inp2:
            inp.append(i.strip())
        for i in inp1:
            for j in inp:
                if i==j:
                    out=j.title()
                    out_list.append(out)
                    break
                else:
                    if i not in out_list and i not in inp:
                        out_list.append(i)
        ou=' '.join(out_list)
        return ou