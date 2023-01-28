# Flashcards_First_Complete_Version.py
"""
This program will show the user flashcards and they can interact with it.
Depending on the user input, they can test themselves on each flashcard or they
can quit at any time.
"""



from random import *
import csv
from typing import Counter

def file_to_dictionary(filename):
    file = open(filename, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary

glossary = file_to_dictionary('glossary.txt')



key_list = list(glossary)


def show_flashcard():
    random_key = choice(key_list)
    print("Define: " + random_key)
    input('Press enter to see the definition.')
    print(glossary[random_key])
    after_question()
    
qcounter =  0
    
counter = 0

def after_question():
    global counter
    global qcounter
    qcounter += 1
    after_input = input("Type 'y' if you got it right, 'n' if you didn't.       ")
    if after_input == 'y':
        print("Keep it going, you're doing good.")
        counter +=1
    elif after_input == 'n':
        print('Unlucky. Keep trying.')
    else:
       print("You need to enter either 'y' or 'n'.")


global answer


exit = False


while not exit:
    user_input = input("Enter 's' to show flashcard and 'q' to quit.       ")
    if user_input == 'q':
        print("You got " + str(counter) + " correct out of " + str(qcounter))
        exit = True  
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.       ')

        

























    






    

    

