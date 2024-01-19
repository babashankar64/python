inp =''
while True:
    inp = input()
    if inp.isdigit():
        print(inp,"is number")
        break

inp = ''
while not inp.isdigit():
    inp = input()
print(inp, ' is number')

fr = open('hi.txt','r')
out = fr.read()
print(out)
print(fr)
fr.close()

fr = open('hi.txt','r')
out = fr.readlines()
print(out)
fr.close()


fr = open('hi.txt','r')
out = fr.readline()
print(out)
fr.close()

fr = open('hi.txt','r')
for i in fr:
    i=i.strip()
    print(i)
# fr.close()

fr = open('hi.txt','r')
out = fr.readline()
out1=fr.readlines()
print(out)
print(out1)
fr.close()

fr = open(r'I:\EXPERIENCE LETTER\md5sum.txt','r')
out = fr.readline()
print(out)
for i in fr:
    i = i.strip()
    print(i)
fr.close()
import re
fr = open(r'E:\pycharm\pythonProject3\1801\hi\write.txt','w')
fr.write('3 10 20 30')
# fr.write('i am\n')
# fr.write('ba\nba')
fr.close()
fr = open(r'E:\pycharm\pythonProject3\1801\hi\write.txt','r')
out = fr.readline()
print(out)
out1 = re.split('[ ]', out,1)
out2 = re.split('[:]', out1[1])
# out1 = out.split(' ')
print(out1[0])
print(out2)
fr.close()

fr = open(r'I:\EXPERIENCE LETTER\hi.txt','r')
fw = open(r'I:\EXPERIENCE LETTER\hi1.txt','w')
out = fr.readlines()
for i in out:
    i = i.strip()
    if i.isdigit():
        i=i.strip()
        fw.write(i)
        fw.write('\n')
print(out)
fr.close()
fw.close()
