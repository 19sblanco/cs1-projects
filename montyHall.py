'''
Requirement specification
    This program will simulate a game show 100,000 times. In this game show the 
    contestant picks a door of three and then the host reveals another door that 
    he know is wrong then asks the contestant if they want to switch their answer.
    This program will determine using randomization of their pick to determine if 
    switching or staying is the better choice
'''
'''
system analysis
    no formulas
'''
'''
system design
    1. make while loop over everything
         a. this is so the game can be replayed however many times the user wants
         b. set counter for wins and losses, so they reset with every iteration
    1. prompt user for switching or staying
    
    2. start off program with if they stay
    3. randomly pick winning door 100,000 times
    4. have system randomly pick from three doors 100,000 times
    5. have system keep track of how many times it won and display as percent
    
    6. then program what will happen if they choose to switch
    7. randomly have the program select the winning door 100,000 times
    8. then have the program choose a door 100,000 times
    9. have the choice flipped from correct to incorrect and vice-versa 
(simulating switching)
    10. print the results of how many it got correct and the percentange
    
    11. prompt user to play again, y or Y = play again
    12. end game if they answer anything else
'''
import random

play = True
# create while function over everything making it possible to play again
while play:
        '''
    this code will have the program pick a winning door, initail door, and 
    goat door
        '''
        wins = 0
        winDoor = random.randint(1, 3)
        userDoor = random.randint(1, 3)
        goatDoor = random.randint(1, 3)
        
        # make sure goat door isn't the user door or the winning door
        while goatDoor == winDoor or goatDoor == userDoor:
                goatDoor = random.randint(1, 3)
                if goatDoor != winDoor and goatDoor != winDoor:
                        break
        
        '''
        this code will tell user what door they picked and what door has a goat
        behind it. it will then prompt them to switch or stay
        '''
        print("You picked door #" + str(userDoor))
        print("behind door #" + str(goatDoor) + " Is a goat")
        choice = input("Would you like to switch or stay? ").lower()
        
        '''
        this block of code will determine what to do when they stay.
        for staying it will check to see if their choice is == to the win door,
        it will then add a win to the "wins" counter
        '''
        if choice == "stay":
                for games in range(100001):
                        
                        if userDoor == winDoor:
                                wins += 1
        print(wins)
        '''
        this block of code will determine what to do if they pick switch, first 
        we need it to switch to a door that is != goat door and != userDoor, then
        we determine if its a win and add it to the win counter accordingly
        '''

            
        




'''
# display wins and percentange of times won
    winRate = wins / 100000
    percentage = winRate * 100 # determine %
    print("Wins: " + str(wins))
    print("Win Rate: " + str(round(percentage, 2)) + "%") # display % out to 2 decimal points

# Prompt user to play again
    playAgain = input("Would you like to play again? Enter y for yes: ").lower()
    if playAgain == "y":
        play = True
    else:
        play = False
        print("Thanks for playing!")
'''