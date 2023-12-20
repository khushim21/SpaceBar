import time
import pymysql

DRINKS_DATA = {}
PEOPLE_DATA = {}
PREFS_DATA = {}


def connect():
    db = pymysql.connect(
        host="localhost",
        port=33066,
        db="SpaceBar",
        user="root",
        password="password",
        autocommit=True,
    )
    cursor = db.cursor()
    return db, cursor


def read_drinks_from_db():
    db, cursor = connect()
    global DRINKS_DATA
    RETRIEVE_DRINKS_QUERY = "SELECT * FROM drinks"

    try:
        with cursor:
            cursor.execute(RETRIEVE_DRINKS_QUERY)
            drinks_dump = cursor.fetchall()

    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()

    # Dump db drink data into the empty dict
    for id, drink in drinks_dump:
        DRINKS_DATA[id] = drink


def input_add_to_drinks():
    print("What drink do you want to add?")

    try:
        drink_to_be_added = input(">>> ").strip()  # remove whitespace before/after

        while (
            len(drink_to_be_added) == 0
        ):  # check if empty input entered. If it is: prompt again for input
            print("\nCannot add an empty item to the list.")
            drink_to_be_added = input(">>> ").strip()

        if drink_is_dupe(drink_to_be_added):
            print("\nCannot add duplicate entry.")
            return

        else:
            return write_drinks_to_db(drink_to_be_added)

    except Exception as e:
        print(f"ERROR:\n{e}")

    finally:
        return


def write_drinks_to_db(drink_to_be_added):
    db, cursor = connect()
    # The query we send to the db
    sql = "INSERT INTO drinks (drink_name) VALUES (%s)"
    val = drink_to_be_added

    try:
        with cursor:
            cursor.execute(sql, val)
    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()


def drink_is_dupe(drink):
    if drink in DRINKS_DATA.values():
        return True


def read_people_from_db():
    db, cursor = connect()
    global PEOPLE_DATA
    RETRIEVE_PEOPLE_QUERY = "SELECT * FROM people"

    try:
        with cursor:
            cursor.execute(RETRIEVE_PEOPLE_QUERY)
            people_dump = cursor.fetchall()

    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()

    # Dump db drink data into empty PEOPLE_DATA dict
    for id, first_name, last_name, drink_id in people_dump:
        first_name = str(first_name)
        last_name = str(last_name)
        fullname = first_name.strip() + " " + last_name.strip()
        PEOPLE_DATA[id] = fullname


def input_add_to_people():
    print("Who do you want to add?")
    try:

        first_name = input(
            "\nFirst name:\n>>> "
        ).strip()  # remove any leading/trailing whitespace
        while len(first_name) == 0:
            print("\nFirst name cannot be empty. Please retry.")
            first_name = input(">>> ").strip()

        last_name = input("\nLast name:\n>>> ").strip()
        while len(last_name) == 0:
            print("\nLast name cannot be empty. Please retry.")
            last_name = input(">>> ").strip()

        full_name = first_name + " " + last_name

        if is_dupe_name(full_name):
            print(f"\n'{full_name}' is already on the list and cannot be added again.")
            return

        else:
            write_person_to_db(first_name, last_name)
            return

    except Exception as e:
        print(f"ERROR:\n{e}")
        pass

    finally:
        return


def is_dupe_name(full_name):
    if full_name in PEOPLE_DATA.values():
        time.sleep(1)
        return True


def write_person_to_db(first_name, last_name):
    db, cursor = connect()

    sql = "INSERT INTO people (first_name, last_name) VALUES (%s, %s)"
    val = first_name, last_name

    try:
        with cursor:
            cursor.execute(sql, val)
    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()


def read_prefs_from_db():
    db, cursor = connect()
    global PREFS_DATA
    RETRIEVE_PREFS_QUERY = "SELECT first_name, last_name, drink_id FROM people"

    try:
        with cursor:
            cursor.execute(RETRIEVE_PREFS_QUERY)
            prefs_dump = cursor.fetchall()

    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()

    for first_name, last_name, drink_id in prefs_dump:
        fullname = first_name + " " + last_name

        drink_name = DRINKS_DATA.get(drink_id)

        PREFS_DATA[fullname] = str(drink_name)


def faves_write_fave_to_db(person_id, drink_id):
    db, cursor = connect()

    user_id = person_id
    user_pref = drink_id

    sql = "UPDATE people SET drink_id = %s WHERE person_id = %s"
    val = user_pref, user_id

    try:
        with cursor:
            cursor.execute(sql, val)

    except Exception as err:
        print(Exception)

    finally:
        cursor.close()
        db.close()
        return


def db_data_in_str(data):
    """reformats db data dump from dict into string to print on menu"""
    data_list = []
    for id, name in data.items():
        data_list.append(f"{id} | {name}")
    return data_list