import requests

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"
response = requests.get(url)
response.raise_for_status()
data = response.json()

def is_valid_word(w):
    return w in data 