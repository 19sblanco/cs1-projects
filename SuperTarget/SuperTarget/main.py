import target

def main():
    # Setup target
    target.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Super Target")
        print("2) Single Target")
        mode = eval(input("Which mode do you want to play? 1 or 2: "))

        # If they choose 'Super'
        if mode == 1:
            # Ask how many targets to draw
            num = eval(input("How many targets do you want to draw? "))

            # Draw that many targets - call drawSuperTarget()
            target.drawSuperTarget(num)

        # If they choose single
        elif mode == 2:
            # ask location
            centerX, centerY = eval(input("Enter a center point(x, y): "))
            # ask radius keep as string
            radius = input("Enter the radius of the bullseye (blank for default): ")
            # ask number of rings keep as string
            rings = input("Enter the number of rings (blank for default): ")

        # Draw a single target
            if radius == "" and rings == "":
                target.drawTarget(centerX, centerY)
            elif rings == "":
                target.drawTarget(centerX, centerY, eval(radius))
            elif radius == "":
                target.drawTarget(centerX, centerY, rings=eval(rings))
            else:
                target.drawTarget(centerX, centerY, eval(radius), eval(rings))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        # clear drawings if needed
        if response == 2:
            target.reset()

        # decide to play again
        playAgain = response == 1 or response == 2

    # print a message saying thank you
    print("Thanks for playing!")


main()
