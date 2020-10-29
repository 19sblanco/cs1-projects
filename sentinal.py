# Here is a calculator that is a little more robust
# It still has issues though! What are they?
print("Welcome to the Amazing Multiplication Table Calculator")

begNum = eval(input("Enter the beginning number: "))
endNum = eval(input("Enter the ending number: "))
step = eval(input("Enter the step size: "))

numSpace = len(str(endNum * endNum)) + 2
rowHeaderSpace = len(str(endNum)) + 2
totalWidth = rowHeaderSpace + numSpace * ((endNum - begNum) // step + 1)

print(format("Multiplication Table", "^" + str(totalWidth) + "s"))
print()
print(format("", str(rowHeaderSpace)), end="")

for i in range(begNum, endNum + 1, step):
    print(format(i, ">" + str(numSpace) + "d"), end="")
print()

for i in range(0, totalWidth):
    print("-", end="")
print()

for i in range(begNum, endNum + 1, step):
    print(format(str(i) + " |", ">" + str(rowHeaderSpace) + "s"), end="")
    for j in range(begNum, endNum + 1, step):
        print(format(i * j, ">" + str(numSpace) + "d"), end="")
    print()



