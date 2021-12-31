import random

word_list = ["aardvark", "baboon", "camel", "common", "element"]

chosen_word = word_list[random.randint(0,len(word_list) - 1)]
print(chosen_word)