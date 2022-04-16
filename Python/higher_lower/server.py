from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>/')
def check_answer(guess):
    if guess > random_number:
        return f'<p>Too High</p>' \
               f'<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < random_number:
        return f'<p>Too Low</p>' \
               f'<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    else:
        return f'<p>You Got it</p>' \
               f'<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
