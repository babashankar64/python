x=1
y=1
z=1
n=2
l=[]
for i in range(0,x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if (n != i+j+k):
                l.extend([[i,j,k]])

print(l)

while True:
    inp = input('please enter ')
    if inp.isdigit():
        print('yes')
        break

k=0
while True:
    no = input("enter")
    if no.isdigit():
        no = int(no)
    if no in range(1,10):
        print('well')
        k=1
    if k==1:
        break

