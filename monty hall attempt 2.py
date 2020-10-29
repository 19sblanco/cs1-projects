import random

play = True
while play:
    winDoor = random.randint(1, 3)
    userDoor = random.randint(1, 3)
    '''
    make sure goat door != win door and != userdoor
    '''
    goatDoor = random.randint(1, 3)
    while goatDoor == winDoor or goatDoor == userDoor:
        goatDoor = random.randint(1, 3)
        if goatDoor != winDoor and goatDoor != userDoor:
            break
    '''
    this code is for switching or staying
    '''
    print("You picked door #" + str(userDoor))
    print("Their is a goat behind door #" + str(goatDoor))
    choice = input("Would you like to switch or stay doors? ")
    '''
    this code is for if they pick stay
    '''
    if choice == "stay":
        for games in range(1, 100001):
            wins = 0
            '''
            repeat game 100,000 times with user input to stay
            '''
            winDoor = random.randint(1, 3)
            userDoor = random.randint(1, 3)
            goatDoor = random.randint(1, 3)
           
        if userDoor == winDoor:
            wins += 1
        print(wins)
    