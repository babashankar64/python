def remove_all(mylist,x,*tup):
    inp = list(tup)
    inp.append(x)
    for obj in inp:
        while int(obj) in mylist:
            mylist.remove(obj)
    return mylist
data = [10,20,30,20,30,20,20,50,50,70,80,90]
temp = remove_all(data,10)
print(temp)

temp = remove_all(data,50,30,70)
print(temp)