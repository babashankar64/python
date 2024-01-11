# import re
# exp = 'india | uk | usa'
# inp="i am in and uk "
# out = re.search(exp,inp)
# print(out.start())
# print(out.end())
# print(out.group())
# if out:
#     print('found')
# else:
#     print("not found")
#
#
# import re
# exp = 'india (uk | usa)'
# inp="i am in and india uk "
# out = re.search(exp,inp)
# print(out.start())
# print(out.end())
# print(out.group())
# if out:
#     print('found')
# else:
#     print("not found")
#
#
#
# import re
# exp='G[76DFP]K'
# inp="x GMK"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print('not found')
#
# import re
# exp = "G[52M1][0-79A-FI]K"
# inp = 'x G17K'
# out=re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print('nf')
#
#

data= [10,20,9,4,60,50]
m=data[0]
for i in data:
    if i>m:
        m=i
print(m)