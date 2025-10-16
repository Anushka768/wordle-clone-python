''' code for testing wordle clone'''
from wordle_clone import *
words = load_words("targets.txt")
print(words)  
print(choose_word(words)) 
target =  words[choose_word(words)] 
print('target :', target)
letters = [True]*26 
for i in range(5):
    guess = input('Enter guess: ')
    update_letters(letters,target, guess) 
    print (letters)  
    print(score_guess(guess, target , words))