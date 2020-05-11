# ROUGH DRAFT OF IS452 TEXT GAME
# by Rachel Whitman (rfw3)

##setup.
import os
from time import sleep
clear = lambda: os.system('cls') #clears the cmd screen

## variables
pants = True
pen = True
laptop = True
yourclassroom = False
office_choices = ("classroom", "laptop", "pants", "pens")
yes_no = ["yes", "no"]
directions = ["forward","backward","left","right"]

# ------------ PRINTING TEXT SLOW OR FAST ----------
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
def print_slower(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
def print_fast(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.01)

# -------------INTRODUCTION-------------
def introduction():
    global name
    print_slow("Today is the first day of a new semester in the iSchool. You're late for class!\n")
    print_slow("You rush to the iSchool building, heading in the west entrance.\n")
    print_slow("You think to yourself, ")
    print_slower("'Okay, ")
    print_slower(name)
    print_slower(", you got this. Just gotta find my classroom!'\n")
    print_slow("Running through a short hallway and up some stairs, you burst\nthrough some double doors.\n\n")
    firstfloor()

# =======================================
# ==============FIRST FLOOR =============
# =======================================
def firstfloor():
    print_slow("You are standing on the first floor of the iSchool.\n\n")
    print_slow("Ahead of you, there is a set of double doors.\n")
    print_slow("To your right, there is the front office.\n")
    print_slow("To your left, you see a hallway, but you can't see where it ends.\n")
    print_slow("There is a staircase leading down behind you.\n\n")
    print_slow("Which way do you go?\n")
    choice = ""
    while choice not in directions:
        choice = input(">> ")
        if choice == "forward":
            conference_room()
        elif choice == "right":
            front_office()
        elif choice == "left":
            firstfloorhallway()
        elif choice == "backward":
            stairs_to_basement()
        else:
            print_slow("I didn't quite understand that. Try typing 'forward','right','left', or 'backward'.\n")

# ------------ CONFERENCE ROOM --------------
def conference_room():
    clear()
    print("##################################################################################")
    print()
    print("#######################")
    print("#  CONFERENCE ROOM    #")
    print("#######################")
    print()
    print_slow("You walk forward to the double doors and try to pull them open. They are locked.\n")
    print_slow("You look through the windows of the doors and it looks like the lights are off.\n")
    print_slow("Press enter to continue.")
    input(">> ")
    firstfloor()

# -----------FRONT OFFICE-----------
def front_office():
    clear()
    print("##################################################################################")
    print()
    print("#######################")
    print("#     FRONT OFFICE    #")
    print("#######################")
    print()
    print_slow("You walk up to the front office desk. A woman sitting at the desk greets\nyou with a smile.\n")
    print_slower("'Hello!'")
    print_slow(" she says to you.")
    print_slower(" 'How can I help you?'\n")
    print_slow("Which do you want to ask her about?\n\n")
    print_slow(" classroom ~ laptop ~ pants ~ pens  \n\n")
    choice = ""
    while choice not in office_choices or yes_no:
        choice = input(">> ")
        global classroom
        global laptop
        global pants
        global pen
        if choice == "classroom":
            print_slow("You ask the woman where to find your first class. She nods and says, ")
            print_slower("'Of course!'\n'That class is meeting in room 131. If you go down that hallway behind you, through \n")
            print_slower("the door at the end of the hallway, and around the corner, it will be straight ahead.\nYou can't miss it!'\n")
            print_slow("You note her directions. She smiles once more. 'Can I help you with anything else?'\n")
            choice = ""
        elif choice == "laptop":
            if laptop:
                print_slow("For some reason, you ask her where you can borrow a laptop. She sees the one in your\narms ")
                print_slow("and answers slowly, ")
                print_slower("'Why? You've got one just there......'\n")
                print_slow("You shake your head and wonder why you asked that. 'Sorry,' you say. 'Not sure why\nI said that.'\n")
                print_fast("Do you want to ask the woman about anything else?\n")
                choice = ""
            else:
                print_slow("You explain that you are late for class and you left your laptop in your apartment.\n")
                print_slow("She nods and reassures you, 'You can easily check out a laptop at the Help Desk on the\nsecond floor!'\n")
                print_slow("Do you want to ask the woman about anything else?\n")
                choice = ""
        elif choice == "pants":
            if pants:
                print_slow("You ask where she got her pants. She is confused.\n")
                print_slower("'I'm wearing a skirt......")
                print_slow("but I got it from Target, if you really want to know.'\n")
                print_slow("Do you want to ask her about anything else?\n")
                choice = ""
            else:
                print_slow("You frantically ask her where you can find your pants. You explain that you accidentally\n")
                print_slow("left them at the Help Desk and they accidentally gave them to Childish Gambino. 'Have you seen")
                print_slow("him come through here?' you ask.\n")
                print_slow("Despite the absurdity of the situation, the woman doesn't bat an eye. She nods and says to you,\n")
                print_slower("'That can happen sometimes. I think Mr. Gambino was heading downstairs last I saw him.'\n")
                print_slow("Do you want to ask her about anything else?\n")
                choice = ""
        elif choice == "pens":
            if pen:
                print_slow("You ask her if you can take one of the many pens sitting in the cup on her desk.\n")
                print_slow("She nods and says, ")
                print_slower("'Of course! Thank you for asking.'\n")
                print_slow("Do you want to ask her about anything else?\n")
                choice = ""
            else:
                print_slow("You ask her if you can take one of the many pens sitting in the cup on her desk.\n")
                print_slow("She nods and says, ")
                print_slower("'Of course! Thank you for asking.'\n")
                pen = True
                print_fast("Do you want to ask her about anything else?\n")
                choice = ""
        elif choice == "no":
            firstfloor()
            break
        else:
            print_slow("I didn't quite understand that. Try typing 'classroom', 'laptop', 'pants', 'pens',\nor 'no'.\n")

# ------------ 1ST FLOOR HALLWAY-----------
def firstfloorhallway():
    clear()
    print("##################################################################################")
    print()
    print("#######################")
    print("# FIRST FLOOR HALLWAY #")
    print("#######################")
    print()
    print_slow("You head down the hallway, past faculty offices.\n")
    print_slow("A few of the doors are open, but the offices are mostly empty.\n")
    if pants:
        print_slow("As you walk down the hallway, you see Childish Gambino. He is sitting in a chair outside \n")
        print_slow("one of the offices, seemingly waiting to meet with someone. You guys are friends, and you \n")
        print_slow("exchange a fistbump as you pass him. Its casual. You continue to the end of the hallway.\n")
    else:
        print_slow("You come out a door at the end of the hallway, and hurry around a corner.\n")
        print_slow("\nAhead of you, you see your classroom! Room 131.\n")
        print_slow("To your right, you see another set of stairs, this time going up.\n")
        print_slow("To your left, you see an elevator, with a button for going up and down.\n\n")
        print_slow("Where do you go?")
        choice = ""
        while choice not in directions:
            choice = input(">> ")
            if choice == "forward":
                classroom()
            elif choice == "right":
                stairs_to_2ndfloor()
            elif choice == "left":
                elevator()
            elif choice == "backward":
                print_slower("You head back the way you came. . . . . . . \n")
                firstfloor()
            else:
                print_slow("I didn't quite understand that. Try typing 'forward','right','left', or 'backward'.\n")

# ------------ YOUR CLASSROOM -------------
def classroom():
    global yourclassroom
    global laptop
    global pants
    global pen
    if yourclassroom:
        print_slow("You did it! You made it to class with all of your things. Congrats!\n")
    else:
        print_slow("You realize you are missing something...")
        if laptop:
            if pants:
                if pen:
                    yourclassroom = True
                else:
                    print_slow("You are missing your pen! Go back and see if you can find one.\n")
                    print_slow("\nAnd don't come back until you find one!\n")
            else:
                print_slow("You realize you are missing your pants! You look down to see your bare legs.\n")
                print_slow("You think, ")
                print_slower("'Where could I have left my pants?'\n.\n.\n.")
                print_slow("You suddenly realize you left your pants at the Help Desk! Go back and try to track down \n your pants.\n")
                print_slow("\nAnd don't come back until you find them!\n")
        else:
            print_slow("Your laptop! You thought it was just in your arms but it seems to have disappeared. Maybe \n")
            print_slow("you can borrow one from somewhere? Go back and if you can find another laptop.\n")
            print_slow("\nAnd don't come back until you find one!\n")

# ------------ STAIRS TO BASEMENT -------------
def stairs_to_basement():
    print_slow("You run down the stairs and end up on the basement landing!\n")
    print_slower(".\n.\n.\n.\n.")
    basement()

## START
clear()
print("##################################################################################")
print()
print("#######################")
print("#    ROUGH DRAFT 2    #")
print("#######################")
print()
print_slow("Welcome to Rough Draft 2. Enter your name to begin.\n")
name = input(">>")
print_slow("Hello, ")
print_slow(name)
print_slow(". Would you like to read the instructions?\n")
instructions = ""
while instructions not in yes_no:
    instructions = input(">>")
    if instructions == "yes":
        print_slow("Here are the instructions.\n")
        print_slower("Now then, let's get started. . . . . .\n")
        clear()
        introduction()
    elif instructions == "no":
        print_slower("Let's get started, then. . . . . .\n")
        clear()
        introduction()
    else:
        print_slow("I didn't quite understand that. Try typing 'yes' or 'no'.\n")
