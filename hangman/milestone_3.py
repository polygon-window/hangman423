import random

def choose_word():
    word_list = ['Apple', 'Banana', 'Strawberry', 'Pear', 'Kiwi']
    chosen_word = random.choice(word_list)
    return chosen_word

chosen_word = choose_word()

def ask_for_input():
    while True:
        guess = input('Please guess a letter: ')
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in chosen_word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

ask_for_input()
