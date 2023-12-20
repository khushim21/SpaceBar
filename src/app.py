import os
import time
from datetime import datetime

from src.core.formatting.ascii_greeter import greeting_ascii_art, maingreeter
from src.core.formatting.formatting_funcs import create_table, menu_text, new_table
from src.mysql_db import DRINKS_DATA, PEOPLE_DATA, PREFS_DATA, db_data_in_str
from src.mysql_db import faves_write_fave_to_db, input_add_to_drinks, input_add_to_people
from src.mysql_db import read_drinks_from_db, read_people_from_db, read_prefs_from_db


#### Business logic: shallow
#### Classes: deep

def menu():
    """Base menu that displays on program start"""
    os.system("clear")
    greeting_ascii_art()
    menu_text()
    try:
        answer = int(input("\nEnter your selection:\n>>> "))
    except TypeError:
        menu()
    time.sleep(0.500)
    menu_response_handler(answer)

# take menu input
# process menu input (to Menu class method)
# fail gracefully
# massively reduce loc in this file

def menu_response_handler(answer):
    """# Process the users response"""
    print("")
    PRINT_PEOPLE = 2
    PRINT_DRINKS = 3
    ADD_PERSON = 4
    ADD_DRINK = 5
    SET_PREFS = 6
    PRINT_PREFS = 7
    EXIT_APP = 8

    # try:

    if answer == PRINT_PEOPLE:
        read_people_from_db()  # asks db for an updated list of people incase this has changed.
        create_table("people", db_data_in_str(PEOPLE_DATA))
        run_again()

    elif answer == PRINT_DRINKS:
        read_drinks_from_db()
        create_table("drinks", db_data_in_str(DRINKS_DATA))
        run_again()

    elif answer == ADD_PERSON:
        input_add_to_people()
        run_again()

    elif answer == ADD_DRINK:
        input_add_to_drinks()
        run_again()

    elif answer == SET_PREFS:
        faves_set_drink_prefs()

    elif answer == PRINT_PREFS:
        try:
            read_prefs_from_db()
            new_table("drink preferences", PREFS_DATA)

        except Exception as e:
            print(f"ERROR handling menu response:\n{e}")

        finally:
            run_again()

    elif answer == EXIT_APP:
        quit()

    elif answer == "" or " ":
        os.system("clear")
        menu()

    else:
        print("I'm sorry, I didn't understand that response, please try again.\n")
        run_again()


######################################################
############### SET DRINKS PREFERENCES ###############
######################################################

def faves_set_drink_prefs():
    read_people_from_db()
    read_drinks_from_db()

    try:
        create_table("people", db_data_in_str(PEOPLE_DATA))
        person_id = input(
            "\nPlease enter the ID of the user you wish to set drink preferences for:\n>>> "
        )
        faves_check_person_id_valid(int(person_id))

        create_table("drinks", db_data_in_str(DRINKS_DATA))
        drink_id = input("\nPlease enter the ID of your preferred drink.\n>>> ")
        faves_check_drink_id_valid(int(drink_id))

        faves_write_fave_to_db(person_id, drink_id)

    except Exception as e:
        print(f"ERROR:\n{e}")

    finally:
        pass


def faves_check_person_id_valid(person_id):
    if person_id not in PEOPLE_DATA.keys():
        print("I'm sorry, that ID was not recognised. Please enter a valid ID.\n>>> ")
        person_id = input(">>> ")
    return person_id


def faves_check_drink_id_valid(drink_id):
    if drink_id not in DRINKS_DATA.keys():
        print("I'm sorry, that ID was not recognised. Please enter a valid ID.\n>>> ")
        drink_id = input(">>> ")
    return drink_id


# App UX / helper funcs


def run_again():
    """# Prompts user to hit Enter to return to the menu"""
    while True:
        try:
            _ = input("\nPress enter to return to the menu.")
            menu()
        except Exception:
            break


def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# Entry point


def start():
    # read_drinks_from_db()  # now load drinks from db
    # read_people_from_db()
    # read_prefs_from_db()
    # maingreeter()  # display ASCII greeter, waits for any input
    os.system("clear")  # clear screen to refine display
    menu()  # call menu, ASCII replaced by identical art, menu displays underneath


if __name__ == "__main__":
    # TODO: IF NO DATABASE EXISTS, CREATE TABLES
    start()