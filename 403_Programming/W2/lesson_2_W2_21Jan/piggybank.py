class PiggyBank:
    def __init__(self, starting_money):
        self.money = starting_money
#Add money in your piggy bank

    def add_money(self, amount):
        self.money += amount
#Add money to your piggy bank

    def take_money(self, amount):
        if self.money<amount:
#Check if theres enough money
            return "Not enough money!"
#If not enough, say you cant take it
        else:
            self.money -= amount
#Take the money out
            return (f"You now have {self.money} in your piggy bank.")


my_piggy_bank = PiggyBank(10)

my_piggy_bank.add_money(5)

print(my_piggy_bank.take_money(12)) #This should tell you "Not enough money!"

print(my_piggy_bank.take_money(7)) #This will show how much money is left


