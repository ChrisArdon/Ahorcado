import random

word_list = ["aardvark", "baboon", "camel", "common", "element", "andrea", "gisselle"]

chosen_word = word_list[random.randint(0,len(word_list) - 1)]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
display = []





#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")