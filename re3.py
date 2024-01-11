import re
exp = 'in[az][a-z]a'
inp='i am in uk , now i am in india, next month i will is be in usa'
out = re.search(exp,inp)
# print(out.group())
# print(out.start())
# print(out.end())
if out:
    print(out.group())
else:
    print('not found')

