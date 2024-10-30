# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Make a guess by entering a signal letter, you have five attempts to guess the word.

## milestone_3 contains three functions:
- The first 'choose_word()' selects a random word from a list. This word is the stored as a variable. 
- The second function 'ask_for_input()' then asks the user to enter a letter, checks this input is a single alphabetical character and then calls the third function with this character.
- The final function checks if the character entered by the user in the 'ask_for_input()' function is present in the randomly selected word chosen by the 'choose_word()' function.


