from itertools import combinations_with_replacement
inp =input().split()
inp_str=inp[0]
inp_int=int(inp[1])
inp_list=[]
for i in inp_str:
    inp_list.append(i)
out=sorted(inp_list)
# out1=list(combinations_with_replacement(out,inp_int))
# for i in out1:
#     print(''.join(i))

inp_str = input()
inp_list=[]
for i in inp_str:
    inp_list.append(i)
count=1
out=inp_list[0]
for j in range(1,len(inp_list)):
    if not inp_list[j] == inp_list[j-1]:
        out_t=(count,int(inp_list[j-1]))
        out_tuple=tuple(out_t)
        print(out_tuple,end=' ')
        count=1
        out=inp_list[j]
    else:
        count =count+1
output=(count,int(out))
print(tuple(output))

import os
os.rmdir('hi/hi.py/')
os.rename('hi/hi.py/New Text Document.txt','hi/hi.py/hidef.txt')
print(os.chdir(r'1801\hi/hi.py/'))
os.system('dir')
for i,j,k in os.walk('hi'):
    for filename in k:
        out = os.path.join(i,filename)
        print(out, os.path.getsize(filename))
