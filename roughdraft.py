# trying to customize the code from here: https://trinket.io/python/e5a03e7cbc

### SETUP
# code will check if input includes these phrases.
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

### INTRO
name = input("What is your name?\n")
print("Today is the first day of a new semester in the iSchool. You're late for class!")
print("You rush to the iSchool building, heading in the west entrance.")
print("Running through a short hallway and some stairs, you burst through some double doors.")

### START
response = ""
while response not in directions:
    print("In front of you, there are more double doors.")
    print("To your right, the front office.")
    print("To your left, a hallway.")
    print("Behind you, there are stairs leading down.\n")
    response = input("Which way do you go?\nforward/left/right/backward\n")
    if response == "forward":
        print("You walk forward to the double doors and try to pull them open. They are locked.")
        print("You look through the windows of the doors and it looks like the lights are off.")
    elif response == "left":
        print("You turn left and run down the hallway, past faculty offices.")
        print("A few of the doors are open, but no one is inside any of the rooms.")
        print("You come out a door at the end of the hallway, and run around a corner.")
        print("There is your classroom, you found it!")
    elif response == "right":
        print("You turn right and see the front office. A woman sits behind a desk.")
        print("You ask the woman where your class is. She tells you to head down the hallway")
        print("behind you, around the corner and it'll be right in front of you.")
    elif response == "backward":
        print("You turn around and head down the stairs. They are narrow and creak with every step.")
        print("You come out to a landing on the basement floor.")
        print("Ahead of you is a kitchen with barren counters, save for a microwave and an")
        print("industrial coffee maker with a half-full pot. You guess the coffee is cold.")
        print("To your left you see a hallway with windows in the ceiling, the fall sunlight filling the space.")
        print("To your right you see the Center for Children's Books. They are having their annual book sale.")
    else:
        print("Sorry, I didn't understand you. Try typing forward, left, right, or backward to move.")

### THOUGHTS SO FAR
# yeah this can get complicated REAL fast. i think using functions to call on each explorable space would help.
# the spaces will change if you have certain items, though, so i think i need to use True/False statements and
# figure out a good way to save your inventory. maybe there will be easter egg items, as well as the important ones.
# i saw something online about nested dictionaries? maybe that would be easier than calling functions, but im not sure.
# i also saw something about controlling how fast the text appears? rather than it printing so fast, it will make it
# easier to read if its slower.
# more research to be done!!!!!
