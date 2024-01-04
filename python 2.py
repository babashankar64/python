z=0
def comman(a,b):
    print(a)
    print(b)

x=[4,6,7,4]
y=[5,7,3,4]

comman(x,y)
comman("x","z")
comman(10,20)

inp = input()
out=inp.swapcase()
print(out)
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)




string="ABCDCDCDC"
sub_string="CDC"
k1=[]
k2=0

for i in range(len(sub_string),len(string)):
    for j in range(len(sub_string)-1,len(sub_string)):
        if string[i] == sub_string[j] and string[i-1] == sub_string[j-1] and string[i-2] == sub_string[j-2]:
            k1.append(string[i])
            k2=k2+1






if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

def test(**kwargs):
    print("kwargs are", kwargs)
    print("type is",type(kwargs))
d={"india-mysore":50,"hyd-lbnager":5}
test(**d)

def test(**kwargs):
    # print(x,y)
    print(kwargs)
x='india'
test(name=x)