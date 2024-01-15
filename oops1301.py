class Bank:
    counter = 0
    def __init__(self,an,name):
        self.AN=an
        self.NAME=name
        Bank.counter = Bank.counter+1
    def get_counter1(self):
        print("1",self)
        return self.AN
    @classmethod
    def get_counter2(cls):
        print('2',cls)
        return Bank.counter
    @staticmethod
    def add(x,y):
        return x+y
b1= Bank(123,'baba')

print(Bank.counter)
print(b1.get_counter1())
print(b1.get_counter2())
print(Bank.get_counter1(b1))


out = Bank.add(10,20)
print(out)
out2 = b1.add(10,20)
print(out2)

def add (x,y,z):
    return x+y+z
def add(x,y):
    return x+y
out = add(4,6,7)
print(out)