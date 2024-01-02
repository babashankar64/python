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