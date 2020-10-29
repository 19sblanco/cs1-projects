

# create function for bubble sort, id
def bubbleSort():
    didSwap = True
    while didSwap:
        didSwap = False

        # user bubble sort for card id
        for i in range(len(playerHand) - 1):
            if playerHand[i] > playerHand[i + 1]:
                playerHand[i], playerHand[i + 1] = playerHand[i + 1], playerHand[i]
                didSwap = True

    # print results
    for card in playerHand:
        print(card)

