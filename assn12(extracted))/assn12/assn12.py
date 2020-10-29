import turtle
from classes import Face

def main():
   face = Face()
   face.draw_face()
   done = False
   while not done:
       print("Change My Face")
       mouth = "frown" if face.is_smile() else "smile"
       emotion = "angry" if face.is_happy() else "happy"
       eyes = "blue" if face.is_dark_eyes() else "black"
       print("1) Make me", mouth)
       print("2) Make me", emotion)
       print("3) Make my eyes", eyes)
       print("0) Quit")
       menu = eval(input("Enter a selection: "))
       if menu == 1:
           face.change_mouth()
       elif menu == 2:
           face.change_emotion()
       elif menu == 3:
           face.change_eyes()
       else:
           break
   print("Thanks for Playing")
   turtle.hideturtle()
   turtle.done()
main()

