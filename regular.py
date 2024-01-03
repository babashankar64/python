import re
exp = 'india | usa | uk | austria'
s = 'i was in uk , now  i am in india , next month i will be in usa'
out = re.search(exp,s)
print(out)
if out:
    print(out.group())
    print(out.start())
    print(out.end())
else:
    print('not found')

import re

exp = 'gh[^0-6a-z]k'
passward = 'ghzk'
out = re.search(exp, passward)
print(out)
if out:
    print(out.group())
    print(out.start())
    print(out.end())
else:
    print('not found')


exp = 'gh([^0-6]|[a-d])k'
passward = 'ghek'
out = re.search(exp, passward)
print(out)
if out:
    print(out.group())
    print(out.start())
    print(out.end())
else:
    print('not found')







