import requests
import random
import string

def get_random_word():
  url = 'https://random-word-api.herokuapp.com/word'
  params = {
      'number': 1
  }
  response = requests.get(url, params=params)
  data = response.json()
  return data[0].lower()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")

    word = get_random_word()
    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only 1 letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("That letter is not in the word.")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n" + display_word(word, guessed_letters))
            print("You guessed it:", word)
            return

    print("You ran out of attempts.It was:", word)

hangman()
