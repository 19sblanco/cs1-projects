from account import Account

# starter boolean
starter = True

# make while loop, keep looping till exit "8" inputed
done = False

while starter:
# get input from user
    Id = int(input("Id? "))
    balance = int(input("Balance? "))
    interestRate = int(input("Annual Interest Rate? "))
    # if they enter in an invalid input, don't run
    if interestRate > 10 or interestRate < 0:
        print("Invalid")
    else:
        # assign to account and exit loop
        account1 = Account()
        account1.setId(Id)
        account1.setBalance(balance)
        account1.setAnnualInterestRate(interestRate)
        starter = False

# if valid inputs, run
while not done:
    print("(1): Display ID")
    print("(2): Display Balance")
    print("(3): Display Annual Interest Rate")
    print("(4): Display Monthly Interest Rate")
    print("(5): Display Monthly Interest")
    print("(6): Withdraw Money")
    print("(7): Deposit Money")
    print("(8): Exit")
    choice = int(input("Select: "))
    if choice == 1:
        print("ID: " + str(account1.getId()))
    elif choice == 2:
        print("Balance: " + str(account1.getBalance()))
    elif choice == 3:
        print("Annual Interest Rate: " + str(account1.getAnnualInterestRate()) + "%")
    elif choice == 4:
        print("Monthly Interest Rate: " + str(account1.getMonthlyInterestRate()) + "%")
    elif choice == 5:
        print("Monthly Interest: " + str(account1.getMonthlyInterest()))
    elif choice == 6:
        ammount = int(input("How much? "))
        if ammount > account1.getBalance():
            print("Too much!")
        else:
            account1.withdraw(ammount)
            print("Balance: " + str(account1.getBalance()))
    elif choice == 7:
        ammount = int(input("How much? "))
        account1.deposit(ammount)
        print("Balance: " + str(account1.getBalance()))
    elif choice == 8:
        done = True
    else:
        print("please choose a valid number!")



