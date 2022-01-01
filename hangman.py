import random

word_list = ["aardvark", "baboon", "camel", "common", "element", "andrea", "gisselle"]

chosen_word = word_list[random.randint(0,len(word_list) - 1)]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
display = []

#For each letter in the chosen_word, add a "_" to 'display'.
for letter in chosen_word:
    display += "_"
print(display)


#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
word_lenght = len(chosen_word)
for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)