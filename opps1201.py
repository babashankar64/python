# x=list()
# print(x)
class Bank:

    def test1(self,an,name,bank,amount):
        self.AN=an
        self.NAME=name
        self.BANK=bank
        self.AMOUNT=amount
    def get_balance(self):
        return self.AMOUNT
    def set_balance(self,bal,name):
        self.AMOUNT=bal
        self.NAE=name
b1=Bank()
b1.test1(123,'baba','sbi','5000')
b2=Bank()
b2.test1(125,'SHANKAR','SBI','8000')
print(b1.AMOUNT)
print(b2.AMOUNT)
b1.set_balance(600,"bab")
print(b1.get_balance())
print(b1.AMOUNT,b1.NAME,b1.NAE)
print(b1.__dict__)
print(b2.__dict__)
out = getattr(b1,'AMOUNT')
print(out)
setattr(b2,"BRANCH1",'abcd')
print(b2.__dict__)
