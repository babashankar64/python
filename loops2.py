inp = ['ind','usa','uk','germany']
inp= set(inp)
print(inp)
out=[]
for k in inp:
    print(k)
    x=k.upper()
    # out.append(x)
print(out,end=' ')


data = 'google.com'
tmp = sorted(set(data),key =data.index)
for i in tmp:

   out = data.count(i)
   print(',',i, '-',out,end='  ')
