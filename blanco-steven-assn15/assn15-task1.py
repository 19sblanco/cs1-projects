def main():
    baseList = list(range(1, 101))
    list1 = [x for x in baseList if x % 2 == 0]
    print(list1)
    list2 = [x for x in baseList if x % 3 == 0 and x < 50]
    print(list2)
    list3 = [x * 10 for x in baseList if x % 5 == 0 and x > 50]
    print(list3)


main()
