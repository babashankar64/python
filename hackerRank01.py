

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))
k=0
j=0

for i in range(len(a)):
    if a[i] > b[i]:
        k = k+1
    elif a[i] < b[i]:
        j=j+1
    else:
        pass
print(k,j)

import re
exp = "A.*h"
inp = "i am student .what is Ah"
out = re.search(exp,inp)
if out:
    print(out.group())
else:
    print("nf")


import re
exp = '\d\d+\.\d+'
inp = '55.6'
out = re.search(exp,inp)
if out:
    print(out.group())
else:
    print('nf')


n= int(input())
j= list(map(int, input().rstrip().split()))
b = []
for y in range(n):
    b.append(j[y])
l=0
p=0
a=[]
for i in b:
    if i>=l:
        l=i
for m in b:
    if l>m:
        a.append(m)
for k in a:
    if k>p:
        p=k
print(p)


x=['rn1', 'rn2', 'rn3', 'rn4']
y=['ramesh','kiran','ajay']
data = {}
if len(x)>len(y):
	for i in range(len(x)-1):
		data[x[i]]=y[i]
else:
	for i in range(len(y)-1):
		data[x[i]]=y[i]
print(data)