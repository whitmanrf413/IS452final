# import sys,time,random
# # def slow_type(str):
# #     for letter in str:
# #         sys.stdout.write(letter)
# #         sys.stdout.flush()
# #         time.sleep(0.03)
# # slow_type("Welcome to [name of game]. Enter your name to begin.")
# ##########################
from time import sleep
#
# def print_med(txt):
#     for x in txt:                     # cycle through the text one character at a time
#         print(x, end='', flush=True)  # print one character, no new line, flush buffer
#         sleep(0.03)
# print_slow("Welcome to [name of game]. Enter your name to begin.")
# ##########################

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

import textwrap

# print_slow(textwrap.fill("Today is the first day of a new semester at the iSchool. You are a first year student, and you're on your way to your first class of the day: Information, Organization, and Access, taught by someone named Dr. Sage Blanchard. You've never heard of them, and when you were signing up for classes and researching your professors, you couldn't find any useful information about them online. You aren't sure what to expect. . . ."))


#-------- DOOR NOTE --------
def door_note():
    text = textwrap.fill("Today's class will be a lesson in user experience. Your task is to seek out and locate one of the many copies of our class syllabus that I have hidden around the building. Once you locate one, write your name at the top and place it in the folder below.", 50)
    text2 = textwrap.fill("Do not attempt to photocopy a syllabus someone else has already found - I will know.", 50)
    print()
    print()
    print_med(textwrap.indent(text, "        "))
    print()
    print()
    print_med(textwrap.indent(text2, "         "))
    print()
    print()
    print_med(textwrap.indent("Good luck, and I'll see you next week!\n", prefix="        "))
    print_med(textwrap.indent("- Dr. Sage 'Wit' Blanchard'\n\n", prefix="        "))

# #-------- HELP DESK --------
# def helpdesk():
#     catoftheday = textwrap.fill("'WINNER OF THE WEEK: What sorcery is this? Christine Murdock from Tacomma, Washington, shares, `STEVIE is a two-year-old tuxedo kitty with a 'wizard's beard' white chest. He is a goofy boy who enjoys his walks in the backyard investigating the places he's seen birds and bunnies.` She adds that Stevie also never misses an opportunity to practice his powers, though they're still a bit rusty: `He lets us know he wants something by pawing the closest object with one - or both - paws.`'", 55)
#     print()
#     print_med(textwrap.fill("You step up to the iSchool Help Desk. On the counter, you see a Cat-of-the-Day calendar. Today's Cat-of-the-Day is a long-haired black and white cat named Stevie. There is a picture of said cat sitting in some bright spring grass on a sunny day. The description under the picture says:"))
#     print("\n\n\n\n")
#     print_med(textwrap.indent(catoftheday, prefix="        "))
#     print("\n\n\n\n")
#     print_med(textwrap.fill("There is an iSchool graduate student behind the desk. They smile at you and say, "))
#     print_slow(textwrap.fill(" 'Isn't Stevie just the cutest? That Cat-of-the-Day calendar makes my day every shift I work!'", 61))
#     print_med("\n\nYou nod. ")
#     print_slow(textwrap.fill("'Stevie is pretty cute! He looks very adventurous. . . and fluffy!'", 62))
#     print("\n")
#     print_med(textwrap.fill("The grad student chuckles along with you and asks, "))
#     print_slow(textwrap.fill(" 'Is there anything I can help you with?'", 21))
#     print("\n")
#     print_med(textwrap.fill("You ask about your class's syllabus. The grad student nods knowingly as you speak. It seems other people have also thought to come here for help. Unfortunately, the grad student can neither confirm nor deny the possible location of any syllabi. You thank them anyways, and decide to look elsewhere."))
#     print_fast("\n\nPress enter to continue.\n")
#     input("")

#-------- LOUNGE ---------
def lounge():
    global syllabus
    print()
    print_med(textwrap.fill("You walk down the short hallway to the left and step into a lounge area. There is a small kitchen here and you can smell coffee in the air. There is also a table and chairs for a workspace, and some comfy-looking sofas and chairs. You decide to test one out, just to make sure its as comfortable as it seems, and to rest your feet for a moment. You walk over and gently sit down on one of the sofas, across a coffee table from someone who seems to be scrolling through their phone. It doesn't look like they've moved in a while, and you wonder how long they've been in the lounge . . ."))
    print("\n")
    print_med(textwrap.fill("This sofa is pretty comfortable, but it could be better. You adjust your cushion a little, thinking maybe it isn't in the right spot. As you push it backwards further into the couch, you hear a crinkle of paper. You stand and pick the cushion fully off the couch, only to find . . . a syllabus!"))
    syllabus = True
    print("\n")
    print_med(textwrap.fill("You pick up the white sheet of crumpled paper and read the first few lines to make sure it's for your class:"))
    print("\n\n\n")
    print_med(textwrap.indent("505: Information, Organization, and Access", prefix = "        "))
    print()
    print_med(textwrap.indent("Dr. Sage 'Wit' Blanchard", prefix = "        "))
    print()
    print_med(textwrap.indent("Tuesdays and Thursdays 9-11:50am", prefix = "        "))
    print()
    print_med(textwrap.indent("Room 131", prefix = "        "))
    print("\n\n\n")
    print_med(textwrap.fill("It is! You punch the air in triumph and victory. Who knew taking a break to rest your feet could mean your success? You smooth out the paper on the coffee table, grab a pen from your pocket, and quickly scrawl your name in the top right-hand corner."))
    print("\n")
    print_med(textwrap.fill("You glance around to see if anyone noticed your celebration. The person on their phone is still scrolling; they didn't notice a thing."))
    print("\n")
    print_med(textwrap.fill(". . . . Better get back to your classroom and turn this in."))
    print_fast("\n\nPress enter to continue.\n")
    input("")

print(">> left")
lounge()
