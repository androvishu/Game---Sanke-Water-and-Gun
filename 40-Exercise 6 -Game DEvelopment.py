# Exercise 6-Game Development(Snake, Water, Gun )
import random
import datetime
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 125)
voices = engine.setProperty('voice', voices[1].id)


def speak(string):
    engine.say(string)
    engine.runAndWait()


user = 0
computer = 0
i = 5
get_time = datetime.datetime.now().strftime('%I %H %p')
print(f"Date is : {get_time}")
while 1 <= i:
    list_of_item = ["snake", "water", "gun"]
    choice = random.choice(list_of_item)
    print("Your Remaining attempt", i)
    print("Press 1 for snake!\n"
          "Press 2 for water!\n"
          "Press 3 for gun!")
    in1 = int(input("Enter Here:="))
    if in1 == 1 and choice == "water":
        print("Your choice is : Snake")
        print("Computer choice is : Water")
        print("You WON!")
        speak("You WON!")
        user += 1
        i -= 1

    elif in1 == 2 and choice == "gun":
        print("Your choice is : Water")
        print("Computer choice is : Gun")
        print("You WON!")
        speak("You WON!")
        user += 1
        i -= 1


    elif in1 == 3 and choice == "snake":
        print("Your choice is : Gun")
        print("Computer choice is : Snake")
        print("You WON!")
        speak("You WON!")
        user += 1
        i -= 1


    elif in1 == 1 and choice == "snake":
        print("Your choice is : Snake")
        print("Computer choice is : Snake")
        print("Nobody in WON")
        speak("Nobody in WON")
        i -= 1

    elif in1 == 2 and choice == "water":
        print("Your choice is : Water")
        print("Computer choice is : Water")
        print("Nobody in WON")
        speak("Nobody in WON")
        i -= 1

    elif in1 == 3 and choice == "gun":
        print("Your choice is : Gun")
        print("Computer choice is : Gun")
        print("Nobody in WON")
        speak("Nobody in WON")
        i -= 1

    else:
        print("You lose")
        speak("You lose")
        computer += 1
        i -= 1

if user > computer:
    print("You WON!\nYour score is:=", user)
    print("Computer score is:=", computer)
    speak(f"You WON!\nYour score is {user}")
    speak(f"Computer score is {computer}")
elif user == computer:
    print("Both are scores is same")
    speak(f"Both are scores is same")

else:
    print("You Loss!\ncomputer score is:=", computer)
    print("Your score is:=", computer)
    speak(f"You Loss!\ncomputer score is {computer}")
    speak(f"Your score is {user}")
