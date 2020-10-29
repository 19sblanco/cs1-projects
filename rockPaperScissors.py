# Steven blanco
# CS 1400 - 3
# assn 7

'''
requirement specification:
have user play a game of rock paper scissors against a 
'random' computer
'''

'''
system anaysis:
no formulas
'''

'''
system design:
1. have user input 0, 1, or 2 (represents scissor, rock and paper) respectively
2. store number 1 as value
3. have computer randomly choose number between 0 and 2
4. store number 3 as  computerValue
5. define value as rock paper or scissors based on what number it is
6. do the same as 5 but for the computerValue
7. make the only valid input 0, 1 and 2
7. compare user answer to computer answer to find out who won
8. print statement based on who won/lossed/draw
'''

# code

''' 
test 1: passed
input 1 for rock
should display that I choose rock
and act accordingly to what the computer choose

test 2: passed
input 4 and it should display invalid input
'''
import random
print("Play rock, paper, scissors against a computer!")
print("scissors = 0, rock = 1, paper = 2")

# have user input 0, 1 or 2
value = int(input("Enter in a value: "))

# computer value
computerValue = random.randint(0, 2)

# make only valid input is 0, 1 , 2
if not value <= 0 and not value <= 2:
    print("Invalid input")
    exit()

# redefine rock paper scissors
if value == 0:
    value = "scissors"
elif value == 1:
    value = "rock"
elif value == 2:
    value = "paper"
    
if computerValue == 0:
    computerValue = "scissors"
elif computerValue == 1:
    computerValue = "rock"
elif computerValue == 2:
    computerValue = "paper"

# impliment system analysis
# scissors
if value == "scissors":
    if computerValue == "scissors":
        print("The computer is " + computerValue + ". You are " + value + " too. Its a draw")
    elif computerValue == "rock":
        print("The computer is " + computerValue + ". You are " + value + ", You lossed")
    elif computerValue == "paper":
        print("The computer is " + computerValue + ". You are " + value + ", You won")
        
# rock
if value == "rock":
    if computerValue == "scissors":
        print("The computer is " + computerValue + "." +" You are " + value + ", You won.")
    elif computerValue == "rock":
        print("The computer is " + computerValue + ". You are " + value + " too. Its a draw")
    elif computerValue == "paper":
        print("The computer is " + computerValue + ". You are " + value + ", You lossed")

# paper
if value == "paper":
    if computerValue == "scissors":
        print("The computer is " + computerValue + "." +" You are " + value + ", You lossed")
    if computerValue == "rock":
        print("The computer is " + computerValue + ". You are " + value + ", You won")
    if computerValue == "paper":
        print("The computer is " + computerValue + ". You are " + value + " too. Its a draw")