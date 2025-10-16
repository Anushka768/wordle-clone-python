"""This program creates functions to  implement Word 1P13 game which is similar to wordle."""

import random

## first function to load words
def load_words(filename):
    ''' converts a given string file as parameter into a list of words which returns the list if words are good and false for bad words '''
    file = open(filename,'r')
    all_words = [] #emplty list to append the words into 
    
    for line in file:
        word = line.strip() # removes any whitespaces and stores each word(line) in variable word
        
        #appends the word into all_words list only if it has only alphabets and is not empty(i.e has more than 0 letters)
        if word.isalpha() and len(word) > 0: 
            all_words.append(word)
        else:
            return False
        
    file.close()
    
    length_word = len(all_words[0]) # the first word will be 5 letter long
    
    for i in all_words:
        if (len(i)) != length_word: # if all words are not the same length as 1st word, returns false
            return False
    
    return all_words

## second function to randomly choose a word
def choose_word(word_list):
    '''chooses a random word from the list parameter by generating and returning a random index value, only if the list is not empty'''
    if word_list == "" : # condition for empty list
        return False
    
    return random.randint(0, len(word_list)+1)
    

## third function to update the letters available to use
def update_letters(letters, target, guess) :
    ''' takes boolean value for letters parameter, compares it with target word parameter, and takes user guess parameter to give feedback by returning haw many letters have been used and which ones are not in target'''
    for char in guess:
        if char.isalpha():
            index = ord(char.lower()) - ord('a') # to calculate the index of the letter it subtracts the ord of letter (a)
            if char not in target:
                letters[index] = False # if the letter guessed is not in target word then the index of the word is changed to false from true 
                
    return letters

## third function to evluate the guess and tell the player what letter are at correct place    
def score_guess(guess, target, words) : 
    '''evaluates the guess parameter, compares it with target word and word list parameters to return result which shows which letter are not in target, are in wrong spots, and are in correct spot'''
    guess = guess.lower()
    target = target.lower()
    if (guess not in words) or (len(guess) != len(target)): # returns false for wrong guess 
        return False
    
    result=""   # empty string to add the suitable symbol for each letter after comparison
    for i in range(len(guess)):
            if (guess[i]) == (target[i]): # for correct guess
                result += '*'
            elif (guess[i]) in (target): # for correct guess at wrong spot
                result += '?'
            else :   # for wrong guess
                result += '_'
    return result

