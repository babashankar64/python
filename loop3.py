data = ['india','usa','uk','aus','usa','uk','aus','usa','uk','aus']
out =[]
for i in data:
    if out.count(i)==0:
        out.append(i)
print(out)

data =['10','india','30','40']
out=[]
for i in data:
    if i.isdigit()==True:
        ou = int(i)
        out.append(ou)
    else:
        out.append(i  )


print(out)

data = 'i am indian'
data1= sorted(set(data),key = data.index)
for i in data1:
    out = data.count(i)
    print(i,out)

data = {'rno1' : 'baba','rno2' : 'shankar' , 'rno3' : 'hyd'}
out = {}

for i,j in data.items():
    print(j,i)
    out[j]=i
print(out)

for i in range(5,1,-1):
    print(i)
out ={}
for i in range(len(data)):
    out[i]=data[i]
print(out)
