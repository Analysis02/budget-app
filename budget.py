class Budget:

    def __init__(self,**categories):
        self.categories = categories
        print(self.categories)

    def deposit(self,amount,category):
        self.categories[category] = self.categories[category] + amount
        print('You deposited  NGN' ' ' +str(amount)+' '+ 'for '+category)

    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print("Insufficient Funds")
        else:

            self.categories[category] = self.categories[category] - amount
            print('You withdrew  NGN' ' ' +str(amount)+' from '+ category)

    def transfer(self, amount, debitCategory, creditCategory):
        if amount > self.categories[debitCategory]:
            print('Insufficient Funds')
        else:
            self.categories[debitCategory] = self.categories[debitCategory] - amount
            self.categories[creditCategory] =  self.categories[creditCategory] + amount
            print('You transfered NGN' ' ' + str(amount) + ' ' + 'from ' + debitCategory + ' to '+ creditCategory )

    def checkBalance(self,category):
        print('Your '+ category + ' budget balance is NGN' ' ' + str(self.categories[category]))


budget= Budget(food=5000, rent=80000, clothing=25000, entertainment=7500)
budget.deposit(2000,'food')
budget.deposit(20000, 'rent')
budget.deposit(5000,'clothing')
budget.deposit(2000,'entertainment')
budget.withdraw(1000,'food')
budget.withdraw(40000,'rent')
budget.withdraw(2000,'clothing')
budget.transfer(6000,'rent','food')
budget.transfer(4000,'clothing','entertainment')
budget.checkBalance('food')
budget.checkBalance('rent')
budget.checkBalance('clothing')
budget.checkBalance('entertainment')