data = [10,20,20,20,20,30,40,20,20,20,20,20,30,40,20]
out = data.count(20)
for i in range(out):
    data.remove(20)
print(data)
