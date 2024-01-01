data1 = {1:2, 4:5 , 3:9}
data2 ={4:8, 3:10 , 1:15}

#data1 key extract and extract data key
d1 = list(data1)
d2 = list(data2)
l1 = d1+d2
l2=[]
for i in l1:
    if l2.count(i)==0:
        l2.append(i)
print(l2)
d3={}
#compare d1 and d2.
for i in l2:
    if (i in d1) and (i in d2):
        d3[data1[i]]=data2[i]
print(d3)

print('############################')

inp = 'google.com'

out ={}
for i in inp:
    if i not in out:
        out[i]=1
    else:
        out[i]=out[i]+1
l=list(out.keys())
k=list(out.values())

for i in range(len(k)):
    print(l[i],k[i])





inp = 'aaaaggggaaajjj'
z=''
k=0
a=[]
for i in inp:
    if i == z:
        k =k+1
    else:
        z=i
        a.extend((str(k),z))
        k = 1
a.append(str(k))
a.pop(0)
st= ''.join(a)
print(st)

