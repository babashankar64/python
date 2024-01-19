import re
class Bank:
    def __init__(self,account,name,branch,amount):
        self.__AccNo =account
        self.__NAME = name
        self.__BRANCH = branch
        self.__BALENCE = amount
    
    def get_name(self):
        return self.__NAME
    def set_branch(self,branch):
        if re.search('^[A-z]{3}$',str(branch)):
            self.__BRANCH = branch
        else:
            print('erorr')
    
    def get_branch(self):
        return self.__BRANCH
        
class salaryBank(Bank):
    def get_branch(self):
        b1 = super().get_branch()
        return b1
    def deposite(self,amount):
        if type (amount)!= int:
            print('invalid amount provided !',amount)
            return
        if amount<100:
            print('amount must be min rs100/-')
        self.__BALENCE = self.__BALENCE + amount
        return self.__BALENCE  
s1=salaryBank('620','shan','HDF',5300)
s1.deposite(700)
    
print(s1.__dict__)   
     
    
  

