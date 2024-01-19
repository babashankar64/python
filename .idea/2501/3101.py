class Bank():
    def __init__(self,acc_no,name,bank,amount):
        self.__ACC_NO = acc_no
        self.NAME = name
        self.BANK = bank
        self.AMOUNT = amount
    def get_balance(self):
        return self.AMOUNT
class creditCard():
    def creadit_bill (self,bill):
        self.bill =bill
        self.creadit_bil = self.AMOUNT - self.bill
        self.AMOUNT = self.creadit_bil
        return self.creadit_bil
class Deposite():
    def dep_m (self,amt):
        self.amt = amt
        self.dep = self.AMOUNT+self.amt
        self.AMOUNT = self.dep
        return self.dep
class Banking(Bank,creditCard,Deposite):
    def __init__(self,acc_no,name,bank,amount):
        super().__init__(acc_no,name,bank,amount)
        # self.amt= amt
    def re_money(self):
        return super().dep_m(500)

obj = Banking(620,"baba","sbi",5000)
print(obj.dep_m(500))
print(obj.creadit_bill(1000))
print(obj.re_money())