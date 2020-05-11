# ROUGH DRAFT OF IS452 TEXT GAME
# by Rachel Whitman (rfw3)

##setup.
import os
from time import sleep
clear = lambda: os.system('cls') #clears the cmd screen

##variables
syllabus = False
professor = ("intro", "gameplay")

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
