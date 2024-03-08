from colorama import Fore,Style
import json
import random
import requests

with open('words.json', 'r') as file:
    data = json.load(file)

words = data['words']

word = random.choice(words)
if len(list(word)) != 5:
    print("Sorry, there was an error. Please run the program again")

# word = list(word.upper())
word = ['A','L','L','O','T']
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"
response = requests.get(url)
response.raise_for_status()
data = response.json()

print("Welcome to wordle. Enter a 5 letter word.")

while True:

    def is_valid_word(w):
        
        return w in data 

    your_try = input("Enter a 5 letter word: ")

    your_try_list = list(your_try.upper())
    if len(your_try_list) != 5:
        print("\nLength of word should be 5 letters! Please try again...\n")
        continue
    # elif is_valid_word(your_try.lower()) == False:
    #     print("\nPlease enter a valid 5 letter word.\n")
    #     continue

    def style(value,color):
        if color == "green":
            color = Fore.GREEN
        elif color == "red":
            color = Fore.RED
        elif color == "yellow":
            color = Fore.YELLOW
        return(color + value + Style.RESET_ALL)

    def compare_words(a, b):
        the_word = []
        letter_counts = {}
        for char in a:
            letter_counts[char] = letter_counts.get(char, 0)+1

        for i in range(5):
            print("iteration " + str(i))
            # print(letter_counts)
            if a[i] == b[i]:
                the_word.append(style(b[i],"green"))
                letter_counts[b[i]] -= 1
            elif b[i] in letter_counts and letter_counts[b[i]] > 0:
                # print("Count of the letter '" + b[i] + "'" + str(letter_counts[b[i]]))
                the_word.append(style(b[i],"yellow"))
                letter_counts[b[i]] -= 1  # Decrement count
                # print("Count of the letter '" + b[i] + "'" + str(letter_counts[b[i]]))
            elif letter_counts[b[i]] == 0:
                the_word.append(style(b[i],"red"))
            elif b[i] not in a:
                the_word.append(style(b[i],"red"))
        print("".join(the_word))

    compare_words(word, your_try_list)
        

    if word == your_try_list:
        print("You won the game!!! Congrats.")
        quit()