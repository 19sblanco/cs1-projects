def main():
    # empty list to be filled by user
    numList = []

    # sentinal to enter loop
    done = False

    # loop to have user enter while loop until they enter nothing to exit
    while not done:
        number = input("Enter a number, enter nothing if done: ")
        if number == "":
            done = True
        else:
            numList.append(int(number.strip()))

    # display output
    print(numList)

    # find max value by putting it at 0 index
    maxList = [] + numList
    maxVal = 0
    for i in range(len(maxList) - 1):
        if maxList[i] > maxList[maxVal]:
            maxList[i], maxList[maxVal] = maxList[maxVal], maxList[i]


    # loop to find sum of values
    total = 0
    for i in numList:
        total += i

    # find the average
    average = int(total) / int(len(numList))

    # display output
    print("list length: " + str(len(numList)))
    print("max value: " + str(maxList[0]))
    print("min value: " + str(min(numList)))
    print("total: " + str(total))
    print("average: " + str(average))




main()