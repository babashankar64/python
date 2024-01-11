# x=['rn1','baba','rn2','shankar','rn3','srikanth','rn4']
# if len(x)%2==0:
#     d={}
#     for i in range(0,len(x),2):
#         d[x[i]]=x[i+1]
#     print(d)
# else:
#     l=len(x)-1
#     d = {}
#     for i in range(0,l, 2):
#         d[x[i]] = x[i + 1]
#     print(d)
data =[10,4,5,4,2,1,1,2,1]
g=[]
p=[]
for i in range(0,len(data)+1,3):
    k = 0
    if i>0:
        for j in range(i):
            if j not in g:
                g.append(j)
                k=k+data[j]
        p.append(k)
print(p)

# data =[10,20,10,10,10,20,10]
# temp=[]
# for i in data:
#     if i not in temp:
#         temp.append(i)
# print(temp)