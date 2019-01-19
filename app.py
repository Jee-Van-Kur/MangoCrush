try:
    import json
except ImportError:
    import simplejson as json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("\n Did you mean %s instead [y or n]?" %get_close_matches(word, data.keys())[0])

        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("\n Scoop ! No such word yet. ")
    else:
        return("\n Pulp ! No such word found.")


print("\n MangoCrush Terminal Active \n")
word_user = input(" Enter a word: ")

output = meaning(word_user)
print("\n")
if type(output) == list:
    for item in output:
        print("-", item)
else:
    print("-", output)
print("\n")
