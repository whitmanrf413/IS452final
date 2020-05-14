# ROUGH DRAFT OF IS452 TEXT GAME
# by Rachel Whitman (rfw3)

#setup
import os
import sys
import textwrap
from time import sleep
clear = lambda: os.system('cls') #clears the cmd screen

##variables
syllabus = False
menu_choices = ["menu", "instructions", "start", "quit"]
directions = ["forward", "left", "right", "backward", "quit"]
floors = ["first floor", "second floor", "basement", "upstairs", "downstairs"]

# ------------ PRINTING TEXT SLOW OR FAST ----------
def print_med(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
def print_fast(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.01)

# ----------- GAME MENU/START -------------
def menu():
    clear()
    print("#############################################################################")
    print("#                                SYLLABUS DAY                               #")
    print("#############################################################################")
    print()
    print_med("Welcome to Syllabus Day, a game made by Rachel Whitman.")
    print_med("\n\nTo read the instructions, type 'instructions' and press enter.\nTo start the game, type 'start' and press enter.\nTo exit the game, type 'quit' and press enter.\n\n")
    input1 = ""
    while input1 not in menu_choices:
        input1 = input(">> ")
        if input1.lower() == "instructions":
            instructions()
            clear()
            introduction()
            break
        elif input1.lower() == "start":
            print_slow("\nLet's get started, then . . . . . .\n")
            clear()
            introduction()
            break
        elif input1.lower() == "quit":
            quit_game()
            break
        else:
            print_med("I didn't quite understand that. Try typing 'instructions', 'start', or 'quit'.\n")

# -------- INSTRUCTIONS --------
def instructions():
    print_med("\nHere are the instructions!\n\n")
    print_med(textwrap.fill("In this game, you will be given a description of your surroundings and then prompted to explore. To move in a certain direction, just type the direction you want to go, and then press enter!"))
    print_med("\n\nYour choices for directions to explore will be one of the following options:\n\n")
    print_med("   ~ forward ~ left ~ right ~ backward ~\n\n")
    print_med(" ~ first floor ~ second floor ~ basement ~\n\n")
    print_med(textwrap.fill("If you ever forget what to type or you mistype something, I'll let you know that I didn't understand you and give you those directions again."))
    print_med("\n\nYou can also type 'quit' in any prompt to exit the game.\n\nNow that you know how the game works, press enter to get started!")
    input("")

# --------- QUIT GAME --------
def quit_game():
    print_slow("\nThanks for playing!\n\n")
    print_slow(". . . . . . . . . . . . . . . . .")
    clear()
    sys.exit()

# ------- INTRODUCTION ---------
def introduction():
    global syllabus
    syllabus = False
    print("#############################################################################")
    print()
    print_med(textwrap.fill("Today is the first day of a new semester at the iSchool. You are a first year student, and you're on your way to your first class of the day: Information, Organization, and Access, taught by someone named Dr. Sage Blanchard. You've never heard of them, and when you were signing up for classes and researching your professors, you couldn't find any useful information about them online."))
    print_slow("\n\nYou aren't sure what to expect. . . .\n\n")
    print_fast("Press enter to continue.\n")
    input("")
    print_med(textwrap.fill("You find your classroom easy enough, but the door is closed and the lights are off. A few other people are standing by the door, reading a piece of paper taped to it. You walk forward to inspect and read along with them, and on the paper is a message written neatly in blue ink:"))
    door_note()
    print_fast("\n\nPress enter to continue.\n")
    input("")
    print_med(textwrap.fill("You notice a manilla envelope taped to the door below the note. You aren't sure if it had been there a moment before. A few white sheets of printer paper are already in the envelope. "))
    print("\n")
    print_slow(textwrap.fill("'How did people already find copies? Class has barely started!'"))
    print_med(" you\nthink to yourself.\n\n")
    print_med(textwrap.fill("The longer you wait, however, the more difficult the search will become, so you better get started!"))
    print_fast("\n\nPress enter to continue.\n")
    input("")
    clear()
    yourclassroom()

#-------- YOUR CLASSROOM --------
def yourclassroom():
    print("#############################################################################")
    print_med("\nYou are standing in front of your classroom, with the door to your back.\n\n")
    print_med("You see some double doors leading to a lecture hall in front of you.\nYou see a hallway to your left.\nYou see a window to your right.\n\n")
    print_med("Which way do you go?\n\n")
    choice = ""
    while choice not in directions:
        choice = input(">> ")
        if choice.lower() == "forward":
            empty_classroom()
        elif choice.lower() == "left":
            print()
            firstfloorhallway()
            break
        elif choice.lower() == "right":
            firstfloorwindow()
        elif choice.lower() == "backward":
            print()
            print_med(textwrap.fill("You turn around and read the note on the door of your classroom once more."))
            door_note()
            print_fast("\n\nPress enter to continue.\n")
            input("")
            yourclassroom()
        elif choice.lower() == "quit":
            quit_game()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'forward', 'backward', 'left', or 'right' to explore. Type 'quit' to exit the game."))
            print("\n")

#-------- DOOR NOTE --------
def door_note():
    text = textwrap.fill("'Welcome to your first day of IS505: Information, Organization, & Access! Unfortunately, I am indisposed this week, so today's class will be a lesson in information retrieval. Your task is to seek out and locate one of the 10 (ten!) copies of our class syllabus that I have hidden around the building. Once you locate one, write your name at the top and place it in the folder below to receive extra credit points to start your semester off strong!", 50)
    text2 = textwrap.fill("Do not attempt to photocopy a syllabus someone else has already found - I will know.", 50)
    print_med("\n\n\n\n")
    print_med(textwrap.indent(text, "   "))
    print_med("\n\n")
    print_med(textwrap.indent(text2, "    "))
    print_med("\n\n")
    print_med(textwrap.indent("Good luck, and I'll see you next week!\n", prefix="   "))
    print_med(textwrap.indent("- Dr. Sage 'Wit' Blanchard'\n\n", prefix="   "))

#------- EMPTY CLASSROOM ------
def empty_classroom():
    print()
    print_med(textwrap.fill("You step towards the double doors that lead into the lecture hall. They're locked. You notice a piece of paper on the right door that looks similar to the one on your classroom. You read it, and gather that whatever class was supposed to meet here has been sent on a similar quest to your own - another class looking for copies of their syllabi around the building! From the note, it seems this class is . . . 590: Comics: Advising Readers. What an interesting class! You'll have to make sure you don't pick up and turn in one of their syllabi instead of your own."))
    print_fast("\n\nPress enter to continue.\n")
    input("")
    yourclassroom()

#------- FIRST FLOOR WINDOW --------
def firstfloorwindow():
    print()
    print_med(textwrap.fill("You walk over to the window and look out over the iSchool parking lot. It's a warm sunny day in August, with just enough of a breeze to keep you cool as you walk around campus. You get lost in your thoughts for a moment."))
    print_slow("\n\n. . . . .\n\n")
    print_med(textwrap.fill("Glancing around the windowsill, you don't see much other than a few leaves that have been tracked in from outside. Finding nothing interesting, you turn back around and decide to look elsewhere."))
    print_fast("\n\nPress enter to continue.\n")
    input("")
    yourclassroom()

# ------- FIRST FLOOR HALLWAY ------
def firstfloorhallway():
    print("#############################################################################")
    print()
    print_med(textwrap.fill("You head down the hallway, past faculty offices. A few of the doors are open, but the offices are mostly empty. You step out of the hallway at the other end . . ."))
    print()
    print()
    firstfloorlobby()

#------ FIRST FLOOR LOBBY -------
def firstfloorlobby():
    global syllabus
    print("#############################################################################")
    print_med("\nYou're standing in a lobby area on the first floor of the iSchool.")
    print_med("\n\nAhead of you is the front office.\n")
    print_med("To your left, you see a set of double doors.\n")
    print_med("To your right, there is a staircase that leads up and down.\n")
    print_med("Behind you is the hallway that leads towards your classroom.\n\n")
    print_med("Which way do you go?\n\n")
    choice = ""
    while choice not in directions:
        choice = input(">> ")
        if choice.lower() == "forward":
            front_office()
            break
        elif choice.lower() == "right":
            stairsfromfirstfloor()
        elif choice.lower() == "left":
            conference_room()
            firstfloorhallway()
        elif choice.lower() == "backward":
            if syllabus:
                print()
                print_med(textwrap.fill("You walk over to your classroom's door and, after having found the class's syllabus and writing your name on it, place the paper in the manilla envelope. You did it! You can rest easy for the next week knowing that you earned those extra credit points."))
                print_fast("\n\nPress enter to continue.\n")
                input("")
                end_game()
            else:
                print()
                print_med(textwrap.fill("You turn around and walk down the hallway towards your classroom."))
                print("\n")
                yourclassroom()
        elif choice.lower() == "quit":
            quit_game()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'forward', 'backward', 'left', or 'right' to explore. Type 'quit' to exit the game."))
            print("\n")

#------- FRONT OFFICE --------
def front_office():
    print()
    print_med(textwrap.fill("You walk up to the front office desk. A woman sitting behind the desk greets you with a warm smile."))
    print_slow("\n\n'Hello!'")
    print_med(" she says to you. ")
    print_slow("'What can I help you with?'\n\n")
    print_med(textwrap.fill("You ask her if she has any copies of the syllabus for your 505 class. Unfortunately, she does not, and you aren't the first person to ask her that. She advises you to check the kitchen downstairs and the graduate lounge upstairs. Better hurry before your classmates find all the other copies!"))
    print_fast("\n\nPress enter to continue.\n")
    input("")
    firstfloorlobby()

#-------- CONFERENCE ROOM --------
def conference_room():
    print()
    print_med(textwrap.fill("You walk over to the set of double doors and try to pull them open, but they are locked. You peer inside, but the lights are off and you can't make anything out other than a long table and a number of office chairs around it in the center of the room. You hope that Dr. Blanchard wouldn't hide a sheet of paper in a locked conference room."))
    print_fast("\n\nPress enter to continue.\n")
    input("")
    firstfloorlobby()

#----- STAIRS FROM FIRST FLOOR ------
def stairsfromfirstfloor():
    print()
    print_med(textwrap.fill("Do you want to go upstairs or downstairs?"))
    print("\n")
    choice1 = ""
    while choice1 not in floors:
        choice1 = input(">> ")
        if choice1.lower() == "upstairs":
            print()
            print_med(textwrap.fill("You turn right and head up the stairs, which spiral sharply and creak under your feet."))
            print_slow("\n\n. . . . . . . . .")
            clear()
            secondfloorlanding()
            break
        elif choice1.lower() == "downstairs":
            print()
            print_med(textwrap.fill("You turn right and head down the stairs, which spiral sharply and creak under your feet."))
            print_slow("\n\n. . . . . . . . .")
            clear()
            basement_landing()
            break
        elif choice1.lower() == "quit":
            quit_game()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'upstairs' or 'downstairs' to explore. Type 'quit' to exit the game."))
            print("\n")

#-------- SECOND FLOOR LANDING -----
def secondfloorlanding():
    print("#############################################################################\n")
    print_med("You are standing on the second floor landing.\n\n")
    print_med("To your right, you see the iSchool Help Desk.\n")
    print_med("To your left down a short hallway, you see a lounge area.\n\n")
    print_med("Which way do you want to go?\n\n")
    choice = ""
    while choice not in directions:
        choice = input(">> ")
        if choice.lower() == "right":
            print_med("\nYou step up to the iSchool Help Desk.")
            helpdesk()
        elif choice.lower() == "left":
            print_med("\nYou head left down the hallway towards the lounge.")
            lounge()
        elif choice.lower() == "backward":
            stairsdownfromsecondfloor()
        elif choice.lower() == "quit":
            quit_game()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'backward', 'left', or 'right' to explore. Type 'quit' to exit the game."))
            print("\n")

#-------- HELP DESK --------
def helpdesk():
    print_med("\n\nHere is a placeholder for the helpdesk description.\n")
    print_fast("\nPress enter to continue.\n")
    input("")
    secondfloorlanding()

#-------- LOUNGE ---------
def lounge():
    global syllabus
    print_med("\n\nHere is a placeholder for the lounge description.")
    print_med("\n\nYou found a copy of the syllabus!!!")
    syllabus = True
    print_fast("\n\nPress enter to continue.\n")
    input("")
    secondfloorlanding()

#----STAIRS DOWN FROM SECOND FLOOR --------
def stairsdownfromsecondfloor():
    print()
    print_med(textwrap.fill("You turn back and head down the stairs. Do you go to the first floor or the basement?"))
    print("\n")
    choicetwo = ""
    while choicetwo not in floors:
        choicetwo = input(">> ")
        if choicetwo.lower() == "first floor":
            print_med("\nYou head down one flight of creaky stairs.\n\n")
            print_slow(". . . . . . . . .")
            clear()
            firstfloorlobby()
            break
        elif choicetwo.lower() == "basement":
            print_med("You head down two flights of creaky stairs.\n")
            print_slow(". . . . . . . . .")
            clear()
            basement_landing()
            break
        elif choicetwo.lower() == "quit":
            quit_game()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'first floor' or 'basement' to explore. Type 'quit' to exit the game."))
            print()

#--------- BASEMENT LANDING -------
def basement_landing():
    print("#############################################################################\n")
    print_med("Here's a placeholder for the basement landing description.")
    print_med("\n\nTo your left, you see the iSchool kitchen.")
    print_med("\nTo your right, you see the Center for Children's Books.")
    print_med("\n\nWhich way do you want to go?\n\n")
    choice = ""
    while choice not in directions:
        choice = input(">> ")
        if choice.lower() == "left":
            kitchen()
        elif choice.lower() == "right":
            ccb()
        elif choice.lower() == "backward":
            stairsupfrombasement()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'left', 'right', or 'backward' to explore. Type 'quit' to exit the game."))
            print("\n")

#----- KITCHEN -------
def kitchen():
    print_med("\nYou get yourself a cup of coffee in the kitchen.")
    print_fast("\n\nPress enter to continue.\n")
    input("")
    basement_landing()

# ------ CCB ----------
def ccb():
    print()
    print_med(textwrap.fill("You head over to the Center for Children's Books, or CCB for short. There's nothing there."))
    print_fast("\n\nPress enter to continue.\n")
    input("")
    basement_landing()

#------ STAIRS UP FROM BASEMENT --------
def stairsupfrombasement():
    print()
    print_med(textwrap.fill("You head back up the stairs. Do you go to the first floor or the second floor?"))
    print("\n")
    choicetwo = ""
    while choicetwo not in floors:
        choicetwo = input(">> ")
        if choicetwo.lower() == "first floor":
            print_med("\nYou head up the creaky stairs to the first floor.")
            print_slow("\n\n. . . . . . . . .")
            clear()
            firstfloorlobby()
            break
        elif choicetwo.lower() == "second floor":
            print_med("\nYou head up the creaky stairs to the second floor.")
            print_slow("\n\n. . . . . . . . .")
            clear()
            secondfloorlanding()
            break
        elif choicetwo.lower() == "quit":
            quit_game()
        else:
           print()
           print_med(textwrap.fill("I didn't quite understand that. Try typing 'first floor' or 'second floor' to explore. Type 'quit' to exit the game."))
           print("\n")

#-------------- END GAME -----------
def end_game():
    clear()
    print("#############################################################################\n\n")
    print_med("Congratulations!\n\n")
    print_med(textwrap.fill("You completed the game!! Great job! Give yourself a pat on the back."))
    print_med("\n\n")
    print_med(textwrap.fill("This game was written and coded in Python 3.7 by Rachel Whitman as her final project in IS452: Foundations of Information Processing. She hopes you enjoyed it!"))
    print_med("\n\nIf you want to go back to the menu, type 'menu'.\nIf you want to play again, type 'start'.\nIf you want to close out the game, type 'quit'.\n\n")
    choice = ""
    while choice not in menu_choices:
        choice = input(">> ")
        if choice.lower() == "menu":
            print_slow("One moment . . . . .")
            clear()
            menu()
            break
        elif choice.lower() == "start":
            print_slow("One moment . . . . .")
            clear()
            introduction()
            break
        elif choice.lower() == 'quit':
            quit_game()
        else:
            print()
            print_med(textwrap.fill("I didn't quite understand that. Try typing 'menu' to go back to the menu, 'start' to restart the game, or 'quit' to exit the game."))
            print()

menu()
