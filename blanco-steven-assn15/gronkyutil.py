paw = ["Rock", "Paper", "Scissors"]
coin = ["Heads", "Tails"]
maxCardValue = 20
# Make sure you understand this to do the opposite conversion!!!
def convertCardToValue(cardValue, cardPaw, cardCoin):
    return 2 * ((cardValue - 1) + (maxCardValue * paw.index(cardPaw))) + \
           coin.index(cardCoin)


