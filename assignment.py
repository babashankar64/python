# 47)
# inp = "#test input#"
# #	   0123456789
# write a program to find position 3nd occurance of 't'
#

inp = "#test input#"
k=0
j=0
for i in range(len(inp)):
    if inp[i]=='t':
        k=k+1
        if k==3:
            j=i
print(j)




inp = "#test input#"
char = input('enter char')
times = int(input("position"))
k=0
j=0
for i in range(len(inp)):
    if inp[i]==char:
        k=k+1
        if k==times:
            j=i
print(j)

import re
exp = '([-9]|1[0-2])'
no='13'

out = re.search(exp,no)
if out:
    print('valid',no)
else:
    print('invalid',no)


import math
import os
import random
import re
import sys


n = int(input())
if 100>=n>=1:
    if n % 2 != 0:
        print("Weird")

    elif n in range(2,5):
        print('Not Weired')
    elif n in range(6,20+1):
        print('Weired')

    else:
        print('Not Weired')






