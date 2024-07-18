class BankAccount:
    def set_details(personal,name, balance = 0):
        personal.name = name       
        personal.balance = balance

    def display(personal):
        print(personal.name, personal.balance)

    def withdraw(personal, amount): 
        personal.balance -= amount


    def deposit(personal, amount):
        personal.balance += amount

firstaccount = BankAccount()
firstaccount.set_details('Harold', 9000)

secondaccount = BankAccount()
secondaccount.set_details('Zayn', 90000)

firstaccount.display()
secondaccount.display()

firstaccount.withdraw(100)
secondaccount.deposit(500)

firstaccount.display()
secondaccount.display()