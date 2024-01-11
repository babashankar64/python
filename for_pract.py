inp = ['india','uk','austria','germany','usa']

l=int(input('enter length'))
for i in inp:
    if len(i)==l:
        print(i)


inp='a6g4a3j3'
for i in inp:
    if (not i.isdigit()):
        k=i
    else:
        for c in range(int(i)):
            print(k,end="")

inp='a6g4a3j3'
for i in range(0,len(inp),2):
    print(inp[i] * int(inp[i+1]),end='')



inp = 6
for i in range(inp):
    print(' '* int((inp-i)/2),end='')
    print('*' * i)
    # print('*'* (i-1))
for i in range(int,0,-1):
    print(' '* int((inp-i)/2),end='')
    print('*' * i)
    # print('*'* (i-1))


n=7
for i in range(1,n+1):
    m=[]
    for k in range(1, i+1):
        m.append(str(k))
    o=''.join(m)
    print(o)

n=7
for i in range(1,n+1):
    m=[]
    for k in range(1, i+1):
        print(k,end='')
    print()

n=7
for i in range(1,n+1):
    m=[]
    for k in range(1, i+1):
        print(i,end='')
    print()

data1={1:2,4:5,3:9}
data2={4:8,3:10,1:15}
d={}
for i in data1:
    if i in data2:
        d[data1[i]]=data2[i]
print(d)

inp='a6g4a3j3'
for i in range(0,len(inp),2):
    out=inp[i]*int(inp[i+1])
    print(out,end='')


inp='aaaaaaggggaaajjj'
current_char=inp[0]
count=1
string_c=''
for i in range(1,len(inp)):
    if inp[i]==current_char:
        count= count +1
    else:
        string_c= string_c + inp[i-1]+str(count)
        current_char = inp[i]
        count=1
string_c= string_c + inp[i-1]+str(count)
print(string_c)




