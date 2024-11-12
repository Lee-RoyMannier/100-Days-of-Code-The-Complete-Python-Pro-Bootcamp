from random import choice
from data import word_list

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

random_word = choice(word_list)
words = []
life = len(random_word) - 1

for i in range(len(random_word)):
    words += "_"

running_game = True

while running_game:
    print(random_word)
    print(words)
    guess = input("Enter a letter: ")

    if guess in random_word:
        for word in range(len(random_word)):
            if random_word[word] == guess:
                words[word] = guess
    else:
        life -= 1
        print(stages[life])

    if life == 0:
        print("You loose, the word was: ", random_word)
        running_game = False

    if not "_" in words:
        print("GG")
        running_game = False
