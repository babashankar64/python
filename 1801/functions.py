def comman(a,b=[0,0,0]):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c
x=[2,4,6]
y=[4,6,8]
c=comman(a=x,)
print(c)
