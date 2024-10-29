import random

word_list = ['Apple', 'Banana', 'Strawberry', 'Pear', 'Kiwi']
word = random.choice(word_list)

guess = input('Please guess a letter: ')

if len(guess) == 1:
    print('Good guess!')
else:
    guess = input('Please guess a letter: ')

print(word_list)
print(word)
