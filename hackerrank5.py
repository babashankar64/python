n= int(input())
j= list(map(int, input().rstrip().split()))
# print(j)
b = []
if 2<=n<=10:
    for y in range(n):
        b.append(j[y])
    l=0
    # print(b)
    out = sorted(set(b))
    print(out[-2])
    p=0
    a=[]
    for i in b:
        if i>=l:
            l=i
    for m in b:
        if l>m:
            a.append(m)
    for k in a:
        if k>p:
            p=k
    print(p)

out = 'baba shankar'
k=out.title()
print(k)