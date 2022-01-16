import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
display = []

#For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(word_length):
    display += "_"


end_of_game = False

#Check guessed letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter
            
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    if guess not in chosen_word:
        lives -= 1
    print(lives)
    
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives <= 0:
        end_of_game = True
        print("You Lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    #Import the stages from hangman_art.py
    print(hangman_art.stages[lives])