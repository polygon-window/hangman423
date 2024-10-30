import random

word_list = ['Apple', 'Banana', 'Strawberry', 'Pear', 'Kiwi']

class Hangman():

    def __init__(self, word_list, num_lives = 5): # Initialise the Hangman game with a list of words and a default number of lives (5) 
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower() # Randomly chooses a word from the list passed as an argument for this instance of the Hangman Class and converts it to lowercase
        self.word_guessed = ['_' for _ in range(len(self.word))] # This is used to represent the players progress in the game by displaying letters they have yet to guess as '_'
        self.num_letters = len(set(self.word)) # Creates a set containing the number of letters in the chosen word
        self.list_of_guesses = [] # Creates a list to record the players guesses
        ''' print(f'word is {self.word} word_guessed is {self.word_guessed}') Used to troubleshoot an issue where the length of self.word and self.word_guessed were not equal '''

    def check_guess(self, guess): # A method within the class to check the user input
        guess = guess.lower() # Converts guess to lower case
        if guess in self.word: # If the letter guessed by the user is in the word
            print(f'Good guess! {guess} is in the word.') 
            for letter in range(len(self.word_guessed)): 
                if self.word[letter] == guess: #  For loop to find the corresponding index of the correct guess within the word
                    self.word_guessed[letter] = guess # then replace the '_' at that index with the letter guessed
                    print(self.word_guessed)
            if guess not in self.list_of_guesses:
                self.num_letters -= 1 # reduce the number of letters left to guess by one, if the guess letter has not been guessed already
            
        else:
            self.num_lives -= 1 # If the guess is incorrect reduce the users lives count by 1
            print(f'Sorry, {guess} is not in the word!')
            print(f'You have {self.num_lives} lives left.')


    def ask_for_input(self):
        
        guess = input('Please guess a letter: ').lower() # Asks the user to enter a letter and converts the input to lowercase
        if not guess.isalpha() or len(guess) != 1: # verifies the user input is alphabetical and a single character
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess) # The input is validated and is passed to the check_guess method
            self.list_of_guesses.append(guess) # The letter is added to list of guesses
            


def play_game(word_list):
    
    game = Hangman(word_list)
    
    while True:
        if game.num_lives <= 0:
            print('You lost!')
            break
        elif game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()

play_game(word_list)