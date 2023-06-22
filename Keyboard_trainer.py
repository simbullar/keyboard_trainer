# This program is a keyboard trainer written in Python.
# It will help users to learn how to type faster and more accurately.
import json

import random
import time

op = open('words.json')
fil = open('data.json')

# List of words to be used in the training session. 

file = json.load(op)
file2 = json.load(fil)
words = (file['words'])

# Welcome message for the user. 
 
name = ""
try:
    name = (file2['name'])
except KeyError:
    print("Welcome to the Keyboard Trainer!")
    print("This program will help you learn how to type faster and more accurately.")
    name = input("What is your name?\n")
    dictionary = {
    "name": name,
    }
    json_object = json.dumps(dictionary, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
        

 # Greet the user by their name.


print("Hello, " + name + "! Let's get started.") 

 # Start the training session. 
while True:  

    # Pick a random word from the list of words.  
    word = random.choice(words)  

    # Display the word to be typed by the user.  
    print("\nType the following word: "+word)  

    # Record the start time of typing.  
    start_time = time.time()  

    # Get input from user and store it in a variable called 'typed_word'.  
    typed_word = input()  

    total_time = time.time() - start_time  

    # Check if typed word is correct or not and display appropriate message accordingly.  
    if typed_word == word:
        print("Correct! You took "+str(round(total_time,2))+" seconds to type that word.")
    else:
            print("Incorrect! The correct word was '"+word+"'.")
            print("You took "+str(round(total_time,2))+" seconds to type that word.")     

    # Ask user if they want to continue or not. If yes, then repeat the loop, else break out of it and end program execution.
    choice = input("\nDo you want to continue (y/n)?\n")
    if choice == 'y':
        continue
    else:
        break
