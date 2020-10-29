class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id
    def setBalance(self, balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12
    def getMonthlyInterest(self):
        return self.__balance - (self.__balance * self.getMonthlyInterestRate())
    def withdraw(self, withdraw):
        self.__balance = self.__balance - withdraw
    def deposit(self, deposit):
        self.__balance = self.__balance + deposit

