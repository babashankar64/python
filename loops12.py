import re
exp = r'^\d+$'
inp = 'hi this is 887 str'
out = inp.split()
for inp in out:
    out = re.search(exp,inp)
    if out:
        print(type(out.group()))


import re
exp = r'\d'
inp = 'test 454 dummy 4783 abcd 36546 '
out = re.findall(exp,inp)
print(out)

import re
exp = 'indi'
inp = 'i am indian'
out = re.search(exp,inp)
if out:
    print(out.group())
else:
    print('nf')



import re
exp = 'india | usa | uk |australia'
inp = 'i was in india, now i am in hyd next month i will be in usa '
out = re.search(exp,inp)
if out:
    print(out.group())
    print(out.start())
    print(out.end())
else:
    print('nf')

def get_key(data,value):

    out= list(data.items())
    out1=[]
    for i in out:
        for j in i:
            out1.append(j)
    inp = out1[(out1.index(value)-1)]
    return inp
data = {'rn1': 'ajay','rn2': 'kiran','rn3': 'ramesh'}
out = get_key(data,'kiran')
print(out)

data = [11,22,33,44,55,79,45,65,22,22,22,22,55,22,22,33,22]
k={}
n=[]
for i in range(len(data)):
    k[i]=data[i]
    if data[i]== 55 :
        n.append(i)
for i in range(len(n)-1):
    if i!=0 and i!=4:
        k.pop(n[i])
out = list(k.values())
print(out)

inp = ['abc','cd',10,40,'h',90,'60']
out=[]
for i in inp:
    if not str(i).isdigit():
          out.append(i)

print(out)
