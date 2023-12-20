import os
import sys
import time


def greeter(text, pause):
    for word in text.split():
        print("\n" + word, flush=True)  # without flush=True it all prints at once.
        time.sleep(pause)


def greeting_ascii_art():
    print(
        """
   _____                      ____             
  / ____|                    |  _ \            
 | (___  _ __   __ _  ___ ___| |_) | __ _ _ __ 
  \___ \| '_ \ / _` |/ __/ _ \  _ < / _` | '__|
  ____) | |_) | (_| | (_|  __/ |_) | (_| | |   
 |_____/| .__/ \__,_|\___\___|____/ \__,_|_|   
        | |                                    
        |_|                                        
   
    """
    )


def maingreeter():
    os.system("clear")
    greeter("Welcome to the", 1)
    time.sleep(0.5)
    os.system("clear")
    greeting_ascii_art()
    print("Press Enter to access the menu!\n\n")
    _ = input()
