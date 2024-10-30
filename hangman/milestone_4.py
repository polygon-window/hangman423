import random

word_list = ['Apple', 'Banana', 'Strawberry', 'Pear', 'Kiwi']

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f'word is {self.word} word_guessed is {self.word_guessed}')

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for letter in range(len(self.word_guessed)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess 
                    print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word!')
            print(f'You have {self.num_lives} lives left.')


    def ask_for_input(self):
        
        while True:
            guess = input('Please guess a letter: ').lower()
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            
me = Hangman(word_list)
me.ask_for_input()


'''def choose_word():
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

'''