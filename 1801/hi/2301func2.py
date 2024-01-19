data = {'an123':'baba','an455':'shankar','an420':'baba'}
def get_key(mydict,value):
    retrun_list=[]
    for i,j in mydict.items():
        if j==value:
            retrun_list.append(i)
    if retrun_list:
        return retrun_list
    else:
        return 'KEY NOT EXIST'
        
value = 'baa'
out = get_key(data,value)

print(out)

