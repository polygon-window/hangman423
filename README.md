# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Make a guess by entering a signal letter, you have five attempts to guess the word.

## milestone_3 contains three functions:
- The first 'choose_word()' selects a random word from a list. This word is the stored as a variable. 
- The second function 'ask_for_input()' then asks the user to enter a letter, checks this input is a single alphabetical character and then calls the third function with this character.
- The final function checks if the character entered by the user in the 'ask_for_input()' function is present in the randomly selected word chosen by the 'choose_word()' function.


## milestone_4:

milestone_4 contains a class called Hangman. This class contains updated versions of the functions from milestone_3 as class methods.
The 'ask_for_input()' method now checks if the user input is a single alphabetical character, converts it to lowercase, then passes that character to the 'check_guess()' method and adds it to the list of guesses made by the user.

The 'check_guess()' method then checks if that letter is in the randomly selected word, if so then the word_guessed list is updated to show the users progress in the game. If the letter is not in the word, the user will be prompted that their guess was incorrect and that they have lost a life.

## milestone_5:

milestone_5 completes the development of the program. A new function is added called 'play_game()'. This function initiates an instance of the class 'game' before entering a while loop. The while loop checks the progress of the game. If num_lives reaches 0 a message is printed telling the user they lost, altenatively if the number of letters remaining to guess reaches 0 a victory message is printed. If non of these conditions are met the 'ask_for_input()' method is called and the game continues. For this to work effectively I had to remove the While True loop from 'ask_for_input()' method, so that the 'play_game()' function could effectively track the state of the game.
