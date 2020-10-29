'''
    this program will allow users to enter in an amount of cash
    and will convert that into the least amount of coins
'''
# this block of code will allow users to enter in an amount of money and store it as total
total = float(input("Enter in an amount of cash: "))

# this code convert the total into cents
cents = total * 100

# this code will convert the total amount of cents into dollars
# this code will also get the remaining cents
dollars = cents // 100
remain = cents % 100

# this code will convert remain into quarters
# this code will also get the remaining cents
quarters = remain // 25
remain = cents % 25

# this code will convert the remain into dimes
# this code will also get the remaining cents
dimes = remain // 10
remain = cents % 10

# this code will convert the remain into nickels
# this code will also get the remaining cents
nickels = remain // 5
remain = cents % 5

# this code defines the pennies
pennies = remain // 1

# this code will convert the messages into variables that we will later use to print
message = "Your total amount consist of, $" + str(total) + "\n" + "Dollars: " + str(dollars) + "\n" + "Quarters: " + str(quarters) + "\n" + "Dimes: " + str(dimes) + "\n" + "Nickels: " + str(nickels) + "\n" + "Pennies: " + str(pennies)
print(message)