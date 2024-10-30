import random


def choose_word():
    word_list = ['Apple', 'Banana', 'Strawberry', 'Pear', 'Kiwi']
    chosen_word = random.choice(word_list)
    return chosen_word

while True:
    user_guess = input('Please guess a letter: ')

    if len(user_guess) == 1:
        print('Good guess!') 
        break
    else:
        user_guess = input('Oops! That is not a valid input.')
        continue
    

