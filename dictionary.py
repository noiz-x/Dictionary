"""
Dictionary

This script implements a basic dictionary application that allows users to
lookup, add, redefine, delete terms, and search for terms based on a phrase.

The script uses a JSON file ('dictionary.json') to store the dictionary data,
which includes terms and their definitions.

Author: ZION

Classes:
    Dictionary: Represents a dictionary and provides various methods to interact
    with the dictionary.

Methods:
    all_items():    Print all the items in the dictionary.
    all_keys():     Print all the keys (terms) in the dictionary.
    dict_update():  Update the dictionary by saving changes to the JSON file.
    lookup():       Lookup a term in the dictionary and display its definition.
    index():        Search for terms that contain a specific phrase.
    define():       Add a new term and its definition to the dictionary.
    remove():       Delete a term from the dictionary.
    redefine():     Modify the definition of an existing term in the dictionary.

Usage:
    Run the script and follow the on-screen instructions to perform various dictionary operations.
    Use the corresponding menu options (1-5) to perform specific actions:
        1: Lookup a term
        2: Add a term
        3: Redefine a term
        4: Delete a term
        5: Search for terms based on a phrase
    Use the special characters '`' and '~' to print all keys and items in the dictionary, respectively.
    Enter '0' or 'q' to exit the program.

Note:
    Ensure the 'dictionary.json' file is present in the same directory as this script.
"""

import json
import sys
import pprint

# Open the dictionary from a JSON file
with open("dictionary.json", encoding="utf-8") as dictionary_file:
    dictionary_data = json.load(dictionary_file)


class Dictionary:
    """A dictionary"""

    @staticmethod
    def all_items():
        """Print all dictionary items"""
        pprint.pprint(sorted(dictionary_data.items()))

    @staticmethod
    def all_keys():
        """Print all dictionary keys"""
        print(f"The number of terms in the dictionary is {len(dictionary_data)}")
        pprint.pprint(sorted(dictionary_data.keys()))

    @staticmethod
    def dict_update():
        """Update the dictionary"""
        with open("dictionary.json", "w", encoding="utf-8") as dictionary_file:
            json.dump(dictionary_data, dictionary_file)

    @staticmethod
    def lookup():
        """Lookup a term"""
        term = input("What term do you want to lookup: ").title().strip()
        print("\n")
        print(dictionary_data.get(term, f"I don't know about '{term.lower()}'."))
        if term not in dictionary_data:
            define_term = input("Would you like to define the term (y/n): ")
            if define_term.lower() == "y":
                Dictionary.define()

    @staticmethod
    def index():
        """Search for a term based on a phrase"""
        phrase = input("Enter the phrase to search: ").strip()
        dict_keys_list = list(dictionary_data.keys())
        dict_values_list_f = list(dictionary_data.values())
        dict_values_list = [i.lower() for i in dict_values_list_f]
        print("The following terms contain the phrase:")
        [
            print(" -", dict_keys_list[dict_values_list.index(_)])
            for _ in dict_values_list
            if phrase in _
        ]

    @staticmethod
    def define():
        """Add a term to the dictionary"""
        term = input("What term do you want to define: ").title().strip()
        if term not in dictionary_data:
            definition = input(f"Enter the definition of {term.lower()}: ").strip()
            if definition == "":
                print("You need to define the term!")
            else:
                dictionary_data[term] = definition
                Dictionary.dict_update()
                print(f'A new term "{term.lower()}" has been added to the dictionary.')
        else:
            print(f'"{term.lower()}" already exists in the dictionary!')

    @staticmethod
    def remove():
        """Delete a term from the dictionary"""
        term = input("Enter the term to delete: ").title().strip()
        if term in dictionary_data:
            del dictionary_data[term]
            Dictionary.dict_update()
            print(f'The term "{term.lower()}" has been removed from the dictionary.')
        else:
            print(f'"{term.lower()}" does not exist in the dictionary, so it cannot be deleted!')

    @staticmethod
    def redefine():
        """Redefine the definition of a term"""
        term = input("Which term do you want to redefine: ").title().strip()
        if term in dictionary_data:
            print("\n")
            definition = input("Enter the new definition: ").strip()
            dictionary_data[term] = definition
            Dictionary.dict_update()
            print(f'The definition of "{term.lower()}" has been modified.')
        else:
            print("\n")
            print("That term doesn't exist in the dictionary.")


print("Dictionary".center(50, "="))
while True:
    print("0 - Quit\n1 - Lookup a term\n2 - Add a term\n3 - Redefine a term\n4 - Delete a term\n5 - Index")
    user_input = input('Enter your choice (press "q" to exit): ')
    if user_input in ("0", "q"):
        print("You exited the program.")
        sys.exit(0)

    if user_input == "1":
        Dictionary.lookup()

    elif user_input == "2":
        Dictionary.define()

    elif user_input == "3":
        Dictionary.redefine()

    elif user_input == "4":
        Dictionary.remove()

    elif user_input == "5":
        Dictionary.index()

    elif user_input == "`":
        Dictionary.all_keys()
        print()

    elif user_input == "~":
        Dictionary.all_items()
        print()

    else:
        print("\nInvalid input.\n")
