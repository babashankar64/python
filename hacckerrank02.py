n=int(input())
nam=[]
scor=[]
s=[]
k = {}
for i in range(n):
    name = input()
    score = float(input())
    nam.append(name)
    scor.append(score)
    k[name]=score
out = (sorted(list(set(scor)))[1])
for i in k:
    if k[i]==out:
        s.append(i)
ou = sorted(s)
for i in ou:
    print(i)
