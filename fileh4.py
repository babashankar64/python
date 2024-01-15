fw = open('hi.txt','w')
# h= 'baba'
# fw.write(f'hi i am {h}')
# fw.close()
# print(f'hi {h}')

data = ['hyd','benuluru','karnataka','telangan']

for i in data:
    fw.write(i+'\n')
fw.close()