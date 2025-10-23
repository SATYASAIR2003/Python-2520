class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
        
    def debit(self,amount):
        self.balance -= amount
        print(amount,"RS is debeted and balance is",self.balance)
        
    def credit(self,amount):
        self.balance += amount
        print(amount,"RS is credited and the balance is",self.balance)
        
    def balance1(self):
        return self.balance
        
s1 = Account(100000,'SBI00023517')
print(s1.balance)
print(s1.account_no)
s1.debit(1000)
s1.credit(5000)
print(s1.balance1())