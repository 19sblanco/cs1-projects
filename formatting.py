name = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
fedTax = float(input("Enter federal tax withholding rate: "))
stateTax = float(input("Enter state tax wtihholding rate" ))

# define the variables in the problem
grossPay = hoursWorked * payRate
federalWithholding = fedTax * grossPay
stateWithholding = stateTax * grossPay
totalDeduction = federalWithholding + stateWithholding
netpay = grossPay - totalDeduction

# format output
# chad mano pay info
message = "\n"
message += format(name.upper() + " PAY INFORMATION", "^40s")

# pay
message += "\n\n"
message += format("Pay", "^40s")

#hours worked
message += "\n"
message += format("Hours Worked:", ">28s")
message += format("", ">10")
message += format(hoursWorked, ">2.2f")

# pay rate
message += "\n"
message += format("Pay Rate:", ">28s")
message += format("", ">10")
message += format(payRate, ">2.2f")

# gross pay
message += "\n"
message += format("Gross Pay:", ">28s")
message += format("", ">10")
message += format(grossPay, ">2.2f")
print(message)