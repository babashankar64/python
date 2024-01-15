import re
output = '2343.47893'
input = '([0-9]+)\\.\\d{1,}'
endt= re.search(input,output)
print(endt.group())

import re

exp = r'(\d+)(\d+)\s+\2\1'
inp = '28 82'

endt= re.search(exp,inp)
print(endt.group(2))

exp = r"^\d+$"
inp = 'hi this is 887 str'
out = inp.split(' ')

for inp in out:
    ou = re.search(exp,inp)
    if ou:
        print(ou.group())


import re
exp=r'^[a-z]{3}\d+$'
out = 'i am in  bangulore   pin56006      local'
out= out.split(' ')
for inp in out:
    ou = re.search(exp, inp)
    if ou:
        print(ou.group())

import re
exp = r'([A-z0-9_.]+)@(\w+\.[a-z]+)'
inp = ' test 454 dummy 6756 abcd 892 bab@gmail.com n.p@yohoo.in baba@outlook.com'
exp = r"(\w+)(\s+)(\w+)"
out = re.sub(exp,r'\3\2\1',inp)
# for i in out:
#     print(type(i.group()))
#     # print(i.group(1))
#     # print(i.group(2))

print(out)


inp ="10:20#30%40"
out=re.split('[:#%]+',inp)
print(out)












