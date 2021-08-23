# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demonstrates the purpose of error handling as well
#              as the use of pickling for binary text files
# ChangeLog (Who,When,What):
# ALanger,8.12.21, Created script
# ------------------------------------------------------------------------ #

import pickle

# -- Data -- #
fileName = "BinaryText.txt"  # The name of the data file
choice = ""  # A string that holds the user's choice from the menu
lstData = []  # An empty list that will be filled with the file's contents


# -- Processing -- #
def process(mode, file_name, lst):
    """ Will perform actions on the file depending on the user's choice

            :param mode: (string) with user's choice of action:
            :param file_name: (string) with file name to write to
            :param lst: (list) that holds the file's contents
    """
    if mode == "1":
        lst = read_file(file_name, lst)
        print("Data loaded!")
    elif mode == "2":
        file = open(file_name, "ab")
        text = get_text()
        pickle.dump(text, file)
        file.close()
        print("Write successful!")
    elif mode == "3":
        print("Here is what is currently in the file: ")
        lst = read_file(file_name, lst)
        for item in lst:
            print(item, end="")
        print()
    else:
        print("That is not an option please try again...")


def read_file(file_name, lst):
    """ Will read the contents of the binary file

                :param file_name: (string) with file name to write to
                :param lst: (list) that holds the file's contents
        """
    try:
        file = open(file_name, "rb")
        lst += pickle.load(file)
        file.close()
    except EOFError:
        print("*The specified file is empty*")
    return lst


# -- Input/Output -- #
def get_choice():
    """ Will get the user's choice of action from the menu """
    str_choice = input("Please choose an option from the menu: ")
    return str_choice


def get_text():
    """ Will get the user's text to append to the file """
    text = input("What would you like to add to the file: ")
    return text


# -- Main -- #
while True:
    print("\nMenu:\n1) Load from file\n2) Write to file\n3) See Contents\n4) Exit Program")
    choice = get_choice()
    if choice == "4":
        input("Press enter to exit the program")
        break
    else:
        process(choice, fileName, lstData)

