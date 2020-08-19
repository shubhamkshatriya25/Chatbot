import os
import pyttsx3

chatbot = pyttsx3.init()
chatbot.setProperty('rate',125)
voices = chatbot.getProperty('voices')
chatbot.say("Hey there! I am JARVIS!! , what should I call you?")
chatbot.runAndWait()
name = input("Enter your name: ")
chatbot.say("Hello" + name + "!Hope you are having an amazing day.")
chatbot.runAndWait()
print("\nPress 1 to open Mozilla Firefox")
print("Press 2 to open Notepad")
print("Press 3 to open Google Chrome")
print("Press 4 to open Microsoft Edge")
print("Press 5 to Quit")
chatbot.say("Here's something I can do for you. Please Select your choice!")
chatbot.runAndWait()

# User Interaction
choice = int(input('\nEnter Your Choice: '))
while choice != 5:
    if choice == 1:
        os.system("firefox")
    elif choice == 2:
        os.system("notepad")
    elif choice == 3:
        os.system("chrome")
    elif choice == 4:
        os.system("msedge")
    chatbot.say("Hope you enjoyed your last session.")
    chatbot.runAndWait()
    print("\nPress 1 to open Mozilla Firefox")
    print("Press 2 to open Notepad")
    print("Press 3 to open Google Chrome")
    print("Press 4 to open Microsoft Edge")
    print("Press 5 to Quit")
    chatbot.say("I am still here to assist you. ")
    chatbot.runAndWait()
    choice = int(input('\nEnter Your Choice: '))

chatbot.say("Good Bye" +name+ "!Have an amazing day")
chatbot.runAndWait()