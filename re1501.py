# import re
# exp = 'uk|usa|big( india| world )'
# inp = "i am in big world . next month i will be in usa"
# out = re.search(exp,inp)
# print(out)
# if out:
#     print(out.start())
#     print(out.end())
#     print(out.group())
# else:
#     print('not found')
#
#
# import re
# exp = 'a\w*'
# #[A-zabcd]+ - one or more times
# #[A-zabcd]{1,} - one or more times
# # exp = 'a\w+'
# inp = ("i amaskf in big world . next month i will be in usa. before shopping in Gak")
# #+-means one or more prev expressions
# #* - zero or more prev expressions
# #? - zero or one time
# out = re.search(exp,inp)
# print(out)
# if out:
#     print(out.start())
#     print(out.end())
#     print(out.group())
# else:
#     print('not found')

#
# import re
# exp ='^\d*\.\d*$'
# inp='.'
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print("not found")
#
# import re
# exp = '^\d+\.\d+$'
# inp = '48.34'
# out = re.search(exp,inp)
#
# if out:
#     print(out.group())
# else:
#     print("nf")
#
# import re
# exp = '^hello$'
# inp = 'hello i am baba hello'
# out = re.search(exp,inp)
# print(out)
# if out:
#     print(out.group())
# else:
#     print("nf")
#
# import re
# exp = '[a-z ]+'
# inp= "hello  tesTing"
# out = re.search(exp,inp)
# if out:
#     print(out.group())
# else:
#     print('nf')

import re
exp = '(([a-z]+)(\s*-\s*))(\d+)'
inp = '''covid cases in pin 4850938 bangalore  -  4549 ip'''
out = re.search(exp,inp,flags=re.S)
if out:
    print(out.group())
    print(out.group(1))
    print(out.group(2))
    print(out.group(3))
    print(out.group(4))

else:
    print('nf')