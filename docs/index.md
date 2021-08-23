#### Alison Langer 	
#### August 23, 2021
#### Foundations of Programming: Python
#### Assignment 07
# A Demonstration of Error Handling and Pickling
## Introduction
In this paper I will discuss the process of creating a to do list python script for assignment 07. The assignment requested a python script file that demonstrates the use of error handling and pickling for binary text files. This included four main concepts of user input/output, file I/O, try-except clauses, and pickling. This paper will begin with the initial file creation and will follow through to the final completion of the assignment with the functioning code. 
### Creating a Script File 
The first step for this assignment was to create a folder called “Assignment07” in the C: drive of the computer as a subfolder of the “_PythonClass”.

The next step was to create a new PyCharm project in the “Assignment07” folder. 
 
The first step I took in writing the code for this assignment was creating a header to give a description of the project as well as provide a change log for updates to the code.
```
# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demonstrates the purpose of error handling as well
#              as the use of pickling for binary text files
# ChangeLog (Who,When,What):
# ALanger,8.12.21, Created script
# ------------------------------------------------------------------------ #
```
### Writing the Python Code
To begin my project, I started by writing some lines of initial set up. This included importing the pickle module for binary file IO as well as declaring some variables in the data portion of my script. 
```
import pickle

# -- Data -- #
fileName = "BinaryText.txt"  # The name of the data file
choice = ""  # A string that holds the user's choice from the menu
lstData = []  # An empty list that will be filled with the file's contents
```
Next I defined a method I called “process” which will process the user’s choice from the menu and perform the appropriate actions to fulfill their request.
```
# -- Processing -- #
def process(mode, file_name, lst):
    """ Will perform actions on the file depending on the user's choice

            :param mode: (string) with user's choice of action:
            :param file_name: (string) with file name to write to
            :param lst: (list) that holds the file's contents
    """
```
The “process” method consisted of a series of if-elif-else statements that performed the required actions for the user’s requests. The first if statement loaded the data, the second statement writes what the user specifies to the file, the third statement displays what is currently in the file and the else statement is a default clause for error handling. If the user tries to choose a menu option that is not available, the program will display a message saying, “That is not an option please try again…” and the program will revert back to the menu.For writing to the file I used the pickle function “.dump”. 
```
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
```
For my second processing function, I defined a function called “read_file” that will process the contents of the binary text file. By using the pickle import, I was able to call the “.load” function on pickle to read from the file. I also included a try-except clause here for error handling. From previous experience I know that programs frequently have problems when reading from an empty file. By using an “except EOFError” or a end-of-file error clause, I could print a separate message when the file was empty instead of the program crashing.
```
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
```
Next, I wrote a two Input/Output functions for organization and to reduce redundancy. The first function was called “get_choice” which essentially just prompts the user to choose a menu option and returns that choice to the function it was called from.
```
# -- Input/Output -- #
def get_choice():
    """ Will get the user's choice of action from the menu """
    str_choice = input("Please choose an option from the menu: ")
    return str_choice
```
The second Input/Output function was called “get_text” which was responsible for prompting the user to enter some text to write to the binary file. The function then returned the user’s input to the function it was called from.
```
def get_text():
    """ Will get the user's text to append to the file """
    text = input("What would you like to add to the file: ")
    return text
```
Finally, for my main portion of code I used a while loop to continually print the menu until the user chooses to exit the program. For this I separated choice 4 “Exit Program” in an if statement to check that condition before processing. But first, “get_choice” was called to get the user’s menu choice. If the user didn’t want to exit, then the “process” function was called to perform the required actions to complete the user’s request.
```
# -- Main -- #
while True:
    print("\nMenu:\n1) Load from file\n2) Write to file\n3) See Contents\n4) Exit Program")
    choice = get_choice()
    if choice == "4":
        input("Press enter to exit the program")
        break
    else:
        process(choice, fileName, lstData)
```
### Running the Script 
The final portion of the assignment was to run the Python script in both PyCharm (Fig 1.1 - Fig 1.4) as well as a shell window (Fig 1.5 – Fig. 1.8) and record the running functionality. 

![image](https://user-images.githubusercontent.com/88059657/130528271-679c4db6-0f23-4a7a-b847-371cf6213283.png)

***Fig 1.1 Menu option 1: loading the data from the binary file***

![image](https://user-images.githubusercontent.com/88059657/130528289-840ffd5b-3f57-44b8-b107-0348caa1dd87.png)

***Fig 1.2 Menu option 3: displaying the contents of the binary file***

![image](https://user-images.githubusercontent.com/88059657/130528308-b1930a23-a14e-4af8-a71e-1c35221fdd05.png) 

***Fig 1.3 Menu option 2: writing to the file***

![image](https://user-images.githubusercontent.com/88059657/130528318-d5d85240-9255-4e03-83cf-f15205c675af.png)

***Fig 1.4 Menu option 4: exiting the program***

![image](https://user-images.githubusercontent.com/88059657/130528327-fb31c321-7cf8-4dd6-a360-b3703dbc341b.png)

***Fig 1.5 Menu option 1: loading the data from the binary file***

![image](https://user-images.githubusercontent.com/88059657/130528345-a978136a-b600-4580-9bfc-e51d1b05bb9f.png)

***Fig 1.6 Menu option 3: displaying the contents of the binary file***

![image](https://user-images.githubusercontent.com/88059657/130528353-a804052b-7fae-4225-bc6d-05dcd67251fa.png)

***Fig 1.7 Menu option 2: writing to the file***

![image](https://user-images.githubusercontent.com/88059657/130528364-127a2e7a-953b-4816-a860-bdccf4924b01.png)

***Fig 1.8 Menu option 4: exiting the program***

The last instruction was to verify that the program did write the given information to the specified “BinaryText” text file. This was completed by opening the text file that was created by the program to verify its contents. The contents were there, although unreadable in binary format. (Fig 1.9) 

![image](https://user-images.githubusercontent.com/88059657/130528375-c50ca01c-b763-4d4a-8d35-5cc1d46c43cd.png)

***Fig 1.9 The contents of the “BinaryText” text file***

## Summary 
In this paper discussed the process of creating the to do list script in Python for assignment 07. This script demonstrates the usage of both error handling and pickling for binary text files. This included four main concepts of user input/output, file I/O, try-except clauses, and pickling. Input is useful for obtaining data from the user to utilize in the program. Output is useful for displaying messages or prompts to the user. File I/O can be used to either read or write to a file. In this case we read the binary text from the file and wrote the user’s input to the file as well. Error handling was demonstrated through try-except clauses that were used to detect if the file was empty before reading. For my research on error handling, I used the website [The Python Tutorial](https://docs.python.org/3/tutorial/errors.html) (External Site). Pickling was demonstrated through binary text file IO using the “pickle” import to both load and dump text from the file. For my research on pickling, I used the website [Geeks for Geeks](https://www.geeksforgeeks.org/understanding-python-pickling-example/) (External Site). Throughout my paper I discussed the steps and logic behind each of my decisions while coding the Python script for this assignment and concluded with the final display of the script running in a shell window. 

