# check notes
# ask mano about option 1

from deck import Deck
import gronkyutil

def main():
    deck = Deck()
    playerHand = []

    # deal 30 cards to hand1
    for i in range(30):
        playerHand.append(deck.draw())


    # make a main menu
    MENU = "\n"
    MENU += "1) sort by value\n"
    MENU += "2) sort by id\n"
    MENU += "3) find card\n"
    MENU += "4) new hand\n"
    MENU += "5) quit\n"

    # insert sort
    def insertSort(inputList):
        for i in range(1, len(inputList)):
            currElement = inputList[i]
            j = i - 1
            while j >= 0 and inputList[j].getValue() > currElement.getValue():
                inputList[j + 1] = inputList[j]
                j -= 1

            inputList[j + 1] = currElement

        for card in playerHand:
            print(card)

    # create function for bubble sort, id
    def bubbleSort(inputList):
        didSwap = True
        while didSwap:
            didSwap = False

            # user bubble sort for card id
            for i in range(len(inputList) - 1):
                if inputList[i] > inputList[i + 1]:
                    inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                    didSwap = True

        # print results
        for card in playerHand:
            print(card)

    ##### two functions below go together #####
    # check to see if card in hand
    def search(inputList, key):
        low = 0
        high = len(inputList) - 1

        while high >= low:
            mid = (high + low) // 2
            if key == inputList[mid].getId():
                return mid
            elif key < inputList[mid].getId():
                high = mid - 1
            else:
                low = mid + 1

        return -1


    def checkSearch():
        result = search(playerHand, key)
        if result == -1:
            return False
        else:
            return True
    ###### two functions above go together ######


    # create while loop for menu
    done = False

    while not done:
        # get input from user about menu
        print(MENU)
        choice = int(input(""))

        if choice == 1:
            insertSort(playerHand)

        elif choice == 2:

            bubbleSort(playerHand)

        elif choice == 3:
            # find card

            # user enter value
            value = int(input("Enter a value (between 1 and 20): "))

            # user enter paw from menu
            PawMenu = "\n"
            PawMenu += "0) rock\n"
            PawMenu += "1) paper\n"
            PawMenu += "2) scissors"
            print(PawMenu)

            # pull value from paw list
            paw = gronkyutil.paw[int(input("Enter a paw: "))]

            # user enter coin
            CoinMenu = "\n"
            CoinMenu += "0) heads\n"
            CoinMenu += "1) tails"
            print(CoinMenu)

            # pull value from coin list
            coin = gronkyutil.coin[int(input("Enter a coin: "))]

            # sort list
            bubbleSort()

            # create card, store as key
            key = gronkyutil.convertCardToValue(value, paw, coin)

            # search and checkSearch function
            print(checkSearch())


        elif choice == 4:
            # draw new hand of 30 cards
            deck = Deck()
            playerHand = []

            # deal 30 cards to playerHand
            for i in range(30):
                playerHand.append(deck.draw())

            print("New hand")

        else:
            print("Thanks for playing!")
            done = True


main()