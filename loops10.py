k = int(input('enter'))
k=6

for i in range(k):
    for j in range(i):
        print("*",end="")
    print()
for i in range(6,0,-1):
    print('*' * i)

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end='')

    print()

