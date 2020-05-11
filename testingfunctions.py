# import sys,time,random
# def slow_type(str):
#     for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(0.03)
# slow_type("Welcome to [name of game]. Enter your name to begin.")
##########################
from time import sleep

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
print_slow("Welcome to [name of game]. Enter your name to begin.")
##########################
