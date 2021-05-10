class Atm(object):
    def __init__(self,bank_name,card_number,balance,withdrawal_amount):
        self.bank_name =bank_name
        self.card_number = card_number
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount

    
  

    def balance(self):
        print("balance") 

    def withdrawal_amount(self,gear_type):
        print("withdrawal_amount")


mycard = Atm("Hdfc", "123", "10000", "5000") 
print(mycard.card_number)            
print(mycard.bank_name)
print(mycard.balance)
print(mycard.withdrawal_amount)
     