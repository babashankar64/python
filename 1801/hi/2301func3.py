import re
def con2nums(mylist):
    return_list = []
    exp = "^\d+\.\d+$"
    ex = "^[0-9]+$"
    ex_a = "^[A-Za-z]+$"
    for i in mylist:
        if type(i) == int or type(i) ==float:
            return_list.append(i)
        else:
            if re.search(ex,i):
                return_list.append(int(i))  
            elif re.search(exp,i):
                return_list.append(float(i))
            elif re.search(ex_a,i):
                return_list.append(i)
        
            
    return return_list
data = ['20','30','90']
out = con2nums(data)
print(out)
data= ['20','30','90','ab','4.5',2,2.3]
out = con2nums(data)
print(out)