import json
import random
import compare_words as compare
import is_valid_word as check
import style as style

with open('words.json', 'r') as file:
    data = json.load(file)

words = data['words']

word = random.choice(words)

if len(list(word)) != 5:
    print("Sorry, there was an error. Please run the program again")

word_list = list(word.upper())
counter = 6

print("\nWelcome to wordle. Enter a 5 letter word.")

while True:
    if counter == 0:
        print("Your chances are over. The correct word was " + word)
        print("Please run the program to play again")
        quit()
    your_try = input(f"Enter a 5 letter word(You have {counter} chances left): ")
    your_try_list = list(your_try.upper())

    if len(your_try_list) != 5:
        print("\nLength of word should be 5 letters! Please try again...\n")
        continue
    elif check.is_valid_word(your_try.lower()) == False:
        print("\nPlease enter a valid 5 letter word.\n")
        continue

    compare.compare_words(word_list, your_try_list)
    counter -= 1

    if word_list == your_try_list:
        print("You won the game!!! Congrats.")
        quit()