import PySimpleGUI as sg
import json

import random
import time


op = open('words.json')
fil = open('data.json')

file = json.load(op)
file2 = json.load(fil)
words = (file['words'])
layout1 = [
    [sg.Text("Enter some data")],
    [sg.Text('Name', size = (4, 1)),sg.InputText(key='-NAME-')],
    [sg.Submit("Submit")]
]
try:
    name = (file2['name'])
except KeyError:
    window1 = sg.Window("Text input", layout1)
    while True:
        event, values = window1.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Submit':
            name = values['-NAME-']  # Access the value using the correct key
            # Perform further processing with the name
            dictionary = {
                "name": name,
                }
            json_object = json.dumps(dictionary, indent=4)
            with open("data.json", "w") as outfile:
                outfile.write(json_object)
            
            window1.close()


layout2 = [
    [sg.Text("Keyboard trainer")],
    [sg.Text('', size = (5, 1)),sg.InputText()],
    [sg.Button("Exit")]
    ]


layoutGreet = [
    [sg.Text("Greetings, " + name + "!")],
    [sg.Text("Do you want to proceed?")],
    [sg.Button("Yes")],
    [sg.Button("No")]
]



def my_function():
    window2 = sg.Window("Demo", layout2)
    # Create an event loop
    while True:
        event, values = window2.read()
        #End program if user closes window or
        # presses the OK button

        if event == "Exit " or event == sg.WIN_CLOSED:
            break   
        
        window2.close()

windowGreet = sg.Window("Giga", layoutGreet)

while True:
    event, values = windowGreet.read()
    #End program if user closes window or
    # presses the OK button
    if event == "No " or event == sg.WIN_CLOSED:
        break
    elif event == "Yes":
        break
        my_function()
    windowGreet.close()

 # Start the training session. 
#while True:  

    # Pick a random word from the list of words.  
    #word = random.choice(words)  
    # Display the word to be typed by the user.  
    #print("\nType the following word: "+word)  

    # Record the start time of typing.  
    #start_time = time.time()  

    # Get input from user and store it in a variable called 'typed_word'.  
    #typed_word = input()  

    #total_time = time.time() - start_time  

    # Check if typed word is correct or not and display appropriate message accordingly.  
    #if typed_word == word:
    #    print("Correct! You took "+str(round(total_time,2))+" seconds to type that word.")
    #else:
    #        print("Incorrect! The correct word was '"+word+"'.")
    #        print("You took "+str(round(total_time,2))+" seconds to type that word.")     

    # Ask user if they want to continue or not. If yes, then repeat the loop, else break out of it and end program execution.
    #choice = input("\nDo you want to continue (y/n)?\n")
    #if choice == 'y':
    #    continue
    #else:
    #    break
