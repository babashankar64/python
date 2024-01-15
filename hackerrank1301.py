num=1
numb=(input().split())
numbe = int(numb[0])
number = int(numbe/2)
for i in range(0,number,1):
    print(int((((numbe * 3) - 3) / 2) - (i*3)) *'-', end='' )
    j=int(i + num)
    print(int(i + num)*'.|.', end='')
    num = num + 1
    print((int((((numbe * 3) - 3) / 2)) - (i*3))*'-')

print(int((((numbe*3)-3)/2)-2)*'-',end='')
print('WELCOME',end='')
print(int((((numbe*3)-3)/2)-2)*'-')


num1 = j
for i in range(0,number,1):
    print(int(((i+1)*3))*'-', end="")
    print((num1-i)*'.|.',end='')
    num1 = num1 - 1
    print(int(((i+1)*3))*'-')