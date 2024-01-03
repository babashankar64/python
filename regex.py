import re
exp = '2\d+8'#greedy it will take longest out come
inp  = 'ah c27284348 test 257484278'
out = re.search(exp,inp)
if out:
    print(out.group())
else:
    print('nf')


import re
exp = '2\d+?8'# because of ? will converted into non- greedy
inp  = 'ah c27284348 test 257484278'
out = re.search(exp,inp)
if out:
    print(out.group())
else:
    print('nf')


import re
exp = '^\d+\.\d+$'
inp  = '22.98'
out = re.search(exp,inp)
if out:
    print(out.group())
else:
    print

import re
exp = r'(\d)(\d)\s+\2\1'
inp = '83 38'
out = re.search(exp,inp)
if out:
    print(out.group())
    print(out.group(1))
    print(out.group(2))
    print(out.groups())
else:
    print('nf')


import re
exp = r'(\w{2})(\w{2})(\w{2})\s+\3\2\1'
inp = 'xymbcd cdmbxy'
out = re.search(exp,inp)
if out:
    print(out.group())
    print(out.group(1))
    print(out.group(2))
    print(out.groups())
else:
    print('nf')