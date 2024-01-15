n = int(input())
inp_list = []
for i in range(n):
    i =input().rstrip().split(' ')
    inp_list.append(tuple(i))


out_list=[]
for i in inp_list:
    if i[0] == "insert":
        out_list.insert(int(i[(1)]),int(i[2]))
    if i[0] == "print":
        print(out_list)
    if i[0] == "remove":
        out_list.remove(int(i[1]))
    if i[0] == "append":
        out_list.append(int(i[1]))
    if i[0] == "sort":
        out_list.sort()
    if i[0] == "pop":
        out_list.pop()
    if i[0] == "reverse":
        out_list.reverse()

inp = int(input())
inp_list=[]
for i in range(int(inp)):
    i = input().rstrip().split(' ')
    inp_list.append(i)
for i in inp_list:
    # print(i[0])
    # print(inp_list[-1][0])
    if i[0] == inp_list[-1][0]:
        out = round((int(i[1])+int(i[2])+int(i[3]))/3,2)
        print(out)
import re
inp = int(input())
inp_list = []
for j in range(int(inp)+1):
    data = input().rstrip().split(' ')
    inp_list.append(data)
string = inp_list[-1]
out = ''.join(string)
for i in inp_list:
    if len(i) >= 4 and i[0] == out:

        output=('{:2f}'.format((float(i[1]) + float(i[2]) + float(i[3])) / 3))

input = '[0-9]+.[0-9][0-9]'
endt= re.search(input,output)
print(endt.group())