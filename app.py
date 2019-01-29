import json
import difflib
from difflib import get_close_matches, SequenceMatcher
from flask import Flask, render_template, request

data = json.load(open("data.json"))
x = bool(False)
y = bool(True)

if y:
    print("\n MangoCrush Terminal Active \n Press ^C to exit \n")
    ask = input(" Use as web app ? [y or n] ")

#print(ask)

if(ask == "n"):
    x = True
    print("\n")
elif(ask == "y"):
    # Web app launch
    y = False


# Define web app here
if not x:
    app = Flask(__name__)

    @app.route('/')
    def dictionary():
        return render_template('index.html')

    @app.route('/meaning', methods = ['POST', 'GET'])
    def result():
        if request.method == 'POST':
            result = meaning(request.form['word'])
            return render_template('mango.html', result = result, name = request.form['word'])

    def meaning(word):
        if word.lower() in data:
            return data[word.lower()]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        else:
            return [ "Pulp ! No such word found." ]

    if __name__ == '__main__':
        app.run(debug = False, port = 4996)

#define terminal app here
while x:
    def meaning(word):
        if word.lower() in data:
            return data[word.lower()]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys())) > 0:
            action = input(" Did you mean %s instead ? [y or n]" %get_close_matches(word, data.keys())[0])
            if (action == "y"):
                return data[get_close_matches(word, data.keys())[0]]
            elif (action == "n"):
                return ("\n Scoop ! No such word yet. ")
        else:
            return("\n Pulp ! No such word found.")

    word_user = input(" Enter a word: ")

    output = meaning(word_user)
#    print("\n")
    if type(output) == list:
        for item in output:
            print("-", item)
    else:
        print("-", output)
    print("\n")
