import time
from deck import Deck


def main():
    players = []
    # how many players?
    while True:
        # create extra for dealer
        numPlayers = int(input("How many players?(1-5) "))
        if 0 < numPlayers <= 5:
            for i in range(numPlayers + 1):
                players.append([])
            break
        else:
            continue

    # give each player $100
    playersBalance = []
    for i in range(len(players) - 1):
        playersBalance.append(100)

    # create list for bet amount
    betAmounts = []
    # for i in range(len(players)):
    #     betAmounts.append(None)
    # print(betAmounts)

    # create menu for hitting and holding
    menuHH = "\n 1) hit"
    menuHH += "\n 2) hold\n"

    play = True
    while play:

        # loop for getting bet ammounts
        while True:
            # create instant of deck (shuffle deck each round)
            deck = Deck()

            # user prompt (bet amount)
            for i in range(len(players) - 1):
                # check if lossed
                if playersBalance[i] <= 0:
                    print("\nplayer " + str(i + 1) + " lossed")

                # if still in game
                else:
                    print("\n" + "Player " + str(i + 1) + "\n" + "Current balance: " + str(playersBalance[i]))
                    betAmount = input("Enter a bet (minumum $5): ")

                    # if they don't have minimum required $5
                    if playersBalance[i] < 5:
                        betAmount = playersBalance[i]

                    # functions to check requirements
                    elif not betAmount.isdigit() or not playersBalance[i] >= int(betAmount) >= 5:
                        print("\ninvalid input")
                        while True:
                            betAmount = input("Enter a bet (minumum $5): ")
                            if betAmount.isdigit() and playersBalance[i] >= int(betAmount) >= 5:
                                break

                    print("bet: " + str(betAmount))

                    # add to list
                    betAmounts.append(betAmount)
            # once done getting all the bet ammounts break out of list
            break

        # deal cards
        for i in range(2):
            for j in range(len(players)):
                players[j].append(deck.draw())

        ### player prompt ###.
        playerTotals = []
        for i in range(len(players) - 1):

            # checks if they are still in game
            if playersBalance[i] <= 0:
                continue

            else:
                # show dealers second card
                print("\nDealers Hand")
                print(players[len(players) - 1][1])
                print()

                # display menu and player hand
                print("player " + str(i + 1))
                print(players[i][0])
                print(players[i][1])
                print(menuHH)

                while True:
                    choice = input("")
                    if choice == "1":
                        # display cards
                        players[i].append(deck.draw())
                        for j in players[i]:
                            print(j)

                        # add up card totals
                        total = 0
                        for card in players[i]:
                            if "Ace" in str(card):
                                total += 11
                            elif str(card.getNickName()).isalpha():
                                total += 10
                            else:
                                total += card.getCardValue()

                        # if total is over 21, set aces to 1
                        if total > 21:
                            aceCount = 0
                            for j in players[i]:
                                if "Ace" in str(j):
                                    aceCount += 1
                                    total += 1
                            total -= aceCount * 11
                        print("\t" + str(total))

                        # if they bust
                        if total > 21:
                            message = "╭╮╱╱╱╱╱╱╱╭╮\n"
                            message += "┃┃╱╱╱╱╱╱╭╯╰╮\n"
                            message += "┃╰━┳╮╭┳━┻╮╭╯\n"
                            message += "┃╭╮┃┃┃┃━━┫┃\n"
                            message += "┃╰╯┃╰╯┣━━┃╰╮\n"
                            message += "╰━━┻━━┻━━┻━╯"
                            print(message)
                            playerTotals.append(0)
                            break

                        # if don't bust
                        continue

                    # if they hold
                    elif choice == "2":
                        # determine total of their hand and add to playerTotals list
                        total = 0
                        for card in players[i]:
                            if "Ace" in str(card):
                                # default value 11, unless over 21, then 1
                                total += 11
                            elif str(card.getNickName()).isalpha():
                                total += 10
                            else:
                                total += card.getCardValue()

                        # if total is over 21, set aces to 1
                        if total > 21:
                            aceCount = 0
                            for j in players[i]:
                                if "Ace" in str(j):
                                    aceCount += 1
                                    total += 1
                            total -= aceCount * 11
                        print("\t" + str(total))

                        playerTotals.append(total)
                        break

                    # invalid input
                    else:
                        print("Invalid")
                        continue

        ### dealers turn ###

        # show dealers hand
        print("\nDealers Hand")
        print()
        print(players[-1][0])
        print(players[-1][1])

        # add up card totals
        dealerTotal = 0
        for card in players[-1]:
            if "Ace" in str(card):
                dealerTotal += 11
            elif str(card.getNickName()).isalpha():
                dealerTotal += 10
            else:
                dealerTotal += card.getCardValue()

        # if total is over 21, that means two aces, set 1 to 1
        if dealerTotal > 21:
            dealerTotal = 12

        while dealerTotal < 17:
            # add and display card
            print()
            time.sleep(1)
            print()
            print("Dealer takes card")
            players[-1].append(deck.draw())
            time.sleep(1)
            print(players[-1][-1])


            # add up card totals
            dealerTotal = 0
            for card in players[-1]:
                if "Ace" in str(card):
                    dealerTotal += 11
                elif str(card.getNickName()).isalpha():
                    dealerTotal += 10
                else:
                    dealerTotal += card.getCardValue()

            # if total is over 21, set aces to 1
            if dealerTotal > 21:
                aceCount = 0
                for j in players[-1]:
                    if "Ace" in str(j):
                        aceCount += 1
                        dealerTotal += 1
                dealerTotal -= aceCount * 11

            # if they bust
            if dealerTotal > 21:
                message = "╭╮╱╱╱╱╱╱╱╭╮\n"
                message += "┃┃╱╱╱╱╱╱╭╯╰╮\n"
                message += "┃╰━┳╮╭┳━┻╮╭╯\n"
                message += "┃╭╮┃┃┃┃━━┫┃\n"
                message += "┃╰╯┃╰╯┣━━┃╰╮\n"
                message += "╰━━┻━━┻━━┻━╯"
                print(message)
                dealerTotal = 1
                break

            # if don't bust
            if 17 < dealerTotal < 21:
                print()
                time.sleep(1)
                print("Dealer Holds")
                continue

        # display dealer total
        time.sleep(1)
        print()
        if dealerTotal == 1:
            pass
        else:
            print("Dealer total")
            print(dealerTotal)
        print()

        ### determine winners ###

        # player total vs dealer total
        for i in range(len(players) - 1):
            if playersBalance[i] <= 0:
                pass
            elif playerTotals[i] < dealerTotal:
                print("player " + str(i + 1) + " lost", end=", ")
                playersBalance[i] -= int(betAmounts[i])
                print("Total: ", playersBalance[i])

            elif playerTotals[i] > dealerTotal:
                print("player " + str(i + 1) + " won", end=",  ")
                playersBalance[i] += int(betAmounts[i])
                print("Total: ", playersBalance[i])

            else:
                print("player " + str(i + 1) + " tied", end=", ")
                print("Total: ", playersBalance[i])

        # play again?
        print()

        # if no one has money
        loseCount = 0
        for money in playersBalance:
            if money == 0:
                loseCount += 1
        if loseCount == len(playersBalance):
            again = "n"

        else:
            again = input("Play Again? (Y, N) ")

        if again.lower() == "y":
            for hand in players:
                hand.clear()
            betAmounts.clear()
            continue

        else:
            # end game
            print()
            print("Thanks for playing!")

            # bubble sort
            sort = True
            while sort:
                sort = False

                for i in range(len(playersBalance) - 1):
                    if playersBalance[i] > playersBalance[i + 1]:
                        playersBalance[i], playersBalance[i + 1] = playersBalance[i + 1], playersBalance[i]
                        sort = True

            # display winners
            print()
            for i in range(len(playersBalance) - 1, -1, -1):
                print("player " + str(i + 1) + " $" + str(playersBalance[i]))
                print()

            play = False


main()
