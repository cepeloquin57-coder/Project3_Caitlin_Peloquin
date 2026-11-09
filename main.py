#Part 1
import random

words = ["violin", "garlic", "parrot", "yonder", "travel", "friend", "fridge", "zipper"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
#Part 2
def display_word():
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print('_', end=" ")
def check_game_status(a):
    chars_guessed = 0
    if a >= max_guesses:
        print("You lose!")
        print(f"The word was {secret_word}")
        return "lose"
    for letter in secret_word:
        if letter in guessed_letters:
            chars_guessed += 1
    if chars_guessed == len(secret_word):
        print("You win!")
        print(f"The word was {secret_word}")
        return "win"
    else:
        return "continue"
def play_game():
    incorrect_guesses = 0
    running = True
    while running == True:
        display_word()
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed this letter!")
        else:
            guessed_letters.append(guess)
            if guess not in secret_word:
                incorrect_guesses += 1
            status = check_game_status(incorrect_guesses)
            if status =="win" or status == "lose":
                running = False
            else:
                print(f"You have {max_guesses-incorrect_guesses} guesses left")
#Part 3
play_game()