# IMPORTS
from time import sleep
# ------------ PRINTING TEXT SLOW OR FAST ----------
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
def print_slower(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.01)
def print_fast(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
# -------------INTRODUCTION-------------
def introduction():
    global name
    print_slow("Today is the first day of a new semester in the iSchool. You're late for class!\n")
    print_slow("You rush to the iSchool building, heading in the west entrance.\n")
    print_slow("You think to yourself, 'Okay,")
    print_slower(name)
    print_slower(", you got this. Just gotta find my classroom!")
    print_fast("Running through a short hallway and up some stairs, you burst through some double doors.\n")
    firstfloor()
# =======================================
# ==============FIRST FLOOR =============
# =======================================
def firstfloor():
    print_slow("You are standing on the first floor of the iSchool.\n")
    print_slow("Ahead of you, there is a set of double doors.\n")
    print_slow("To your right, there is the front office.\n")
    print_slow("To your left, you see a hallway, but you can't see where it ends.\n")
    print_slow("There is a staircase leading down behind you.\n")
    print_slow("Which way do you go?")
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
            print_slow("I didn't quite understand that. Try typing 'forward','right','left', or 'backward'.")
# ------------ CONFERENCE ROOM --------------
def conference_room():
    print_slow("You walk forward to the double doors and try to pull them open. They are locked.\n")
    print_slow("You look through the windows of the doors and it looks like the lights are off.\n")
    firstfloor()
# -----------FRONT OFFICE-----------
def front_office():
    print_slow("You walk up to the front office desk. A woman sitting at the desk greets you with a smile.\n")
    print_fast("'Hello!'")
    print_slow(" she says to you.")
    print_fast("'How can I help you?'\n")
    print_slow("Which do you want to ask her about?\n")
    print_slow(office_choices)
    choice = ""
    while choice not in office_choices or yes_no:
        choice = input(">> ")
        global classroom
        global laptop
        global pants
        global pens
        if choice == "classroom":
            print_slow("You ask the woman where to find your first class. She nods and says, 'Of course!\n")
            print_slow("That class is meeting in room 131. If you go down that hallway behind you, through the door\n")
            print_slow("at the end of the hallway, and around the corner, it will be straight ahead. Can't miss it!'\n")
            print_slow("You note her directions. She smiles once more. 'Can I help you with anything else?'\n")
            choice = input(">> ")
        elif choice == "laptop":
            if laptop:
                print_slow("For some reason, you ask her where you can borrow a laptop. She sees the one in your arms\n")
                print_slow("and answers slowly,")
                print_slower("'Why? You've got one just there...'\n")
                print_slow("You shake your head and wonder why you asked that. 'Sorry,' you say. 'Not sure why I said that.'")
                print_fast("Do you want to ask the woman about anything else?")
                choice = input(">> ")
            else:
                print_slow("You explain that you are late for class and you left your laptop in your apartment.\n")
                print_slow("She nods and reassures you, 'You can easily check out a laptop at the Help Desk on the second floor!'\n")
                print_fast("Do you want to ask the woman about anything else?")
                choice = input(">> ")
        elif choice == "pants":
            if pants:
                print_slow("You ask where she got her pants. She is confused.\n")
                print_slower("'I'm wearing a skirt...")
                print_slow("but I got it from Target, if you really want to know.'\n")
                print_fast("Do you want to ask her about anything else?")
                choice = input(">> ")
            else:
                print_fast("You frantically ask her where you can find your pants. You explain that you accidentally\n")
                print_fast("left them at the Help Desk and they accidentally gave them to Childish Gambino. 'Have you seen")
                print_fast("him come through here?' you ask.\n")
                print_slow("Despite the absurdity of the situation, the woman doesn't bat an eye. She nods and says to you,\n")
                print_slow("'That can happen sometimes. I think Mr. Gambino was heading downstairs last I saw him.'\n")
                print_fast("Do you want to ask her about anything else?")
                choice = input(">> ")
        elif choice == "pens":
            if pen:
                print_slow("You ask her if you can take one of the many pens sitting in the cup on her desk.\n")
                print_slow("She nods and says, 'Of course! Thank you for asking.\n")
                print_fast("Do you want to ask her about anything else?")
                choice = input(">> ")
            else:
                print_slow("You ask her if you can take one of the many pens sitting in the cup on her desk.\n")
                print_slow("She nods and says, 'Of course! Thank you for asking.\n")
                pen = True
                print_fast("Do you want to ask her about anything else?")
                choice = input(">> ")
        elif choice == "no":
            firstfloor()
            break
        else:
            print("I didn't quite understand that. Try typing 'classrom', 'laptop', 'pants', 'pens', or 'no'.\n")
# ------------ 1ST FLOOR HALLWAY-----------
def firstfloorhallway():
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
                yourclassroom()
            elif choice == "right":
                stairs_to_2ndfloor()
            elif choice == "left":
                elevator()
            elif choice == "backward":
                print_slower("You head back the way you came. . . . . . . \n")
                firstfloor()
            else:
                print_slow("I didn't quite understand that. Try typing 'forward','right','left', or 'backward'.\n")

# ------------ STAIRS TO BASEMENT -------------
def stairs_to_basement():
    print_slow("You run down the stairs and end up on the basement landing!")
    basement()
# ------------ STAIRS TO 2ND FLOOR ------------
def stairs_to_2ndfloor():
    print_slow("You head up the stairs and come out on the second floor.")
    second_floor()
