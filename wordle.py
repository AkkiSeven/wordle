import json
import random
import compare_words as compare
import is_valid_word as check
import style as style

with open('words.json', 'r') as file:
    data = json.load(file)

words = data['words']

word = random.choice(words)
print(word)

if len(list(word)) != 5:
    print("Sorry, there was an error. Please run the program again")

word = list(word.upper())

print("Welcome to wordle. Enter a 5 letter word.")


while True:


    your_try = input("Enter a 5 letter word: ")

    your_try_list = list(your_try.upper())
    if len(your_try_list) != 5:
        print("\nLength of word should be 5 letters! Please try again...\n")
        continue
    elif check.is_valid_word(your_try.lower()) == False:
        print("\nPlease enter a valid 5 letter word.\n")
        continue



    compare.compare_words(word, your_try_list)
        

    if word == your_try_list:
        print("You won the game!!! Congrats.")
        quit()