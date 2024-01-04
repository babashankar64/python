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