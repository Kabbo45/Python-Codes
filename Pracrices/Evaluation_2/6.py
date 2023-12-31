class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

obj = Account(1122, 20000, 4.5)
obj.withdraw(2500)
obj.deposit(3000)
print("Account ID:", obj.getId())
print("Account Balance: ", obj.getBalance())
print("Monthly Interest Rate: ", obj.getMonthlyInterestRate())
print("Monthly Interest: ", obj.getMonthlyInterest())