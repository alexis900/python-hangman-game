from dataclasses import replace
from random import randint
import os
import platform

HANGMAN_IMAGES = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

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
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

def clearWindow():
    MY_OS = platform.system()
    if MY_OS == "Linux" or MY_OS == "Darwin":
         os.system('clear')
    elif MY_OS == "Windows":
        os.system('cls')


def normaliceWord(word):
    replacements = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u' }
    for a, b in replacements.items():
        word = word.replace(a, b).replace('\n', '')
    return word.upper()


def readFile():
    with open('./data.txt', 'r', encoding='utf-8') as f:
        words = [lines for lines in f]
        f.close()
    return words


def selectWord():
    words = readFile()
    randNum = randint(1, len(words))
    return normaliceWord(words[randNum])


def game():
    word = selectWord()
    print(word)
    lenghtWord = len(word)
    hiddenWord = ['_'] * lenghtWord
    mistakes = 0
    while True:
        print(HANGMAN_IMAGES[mistakes])
        print(*hiddenWord)
        letter = input('Introduce una letra: ').upper()
        try:
            if len(letter) != 1:
                raise TypeError('Lo siento, solo se puede introducir un carácter')
        except TypeError as maxChar:
            print(maxChar)
        else:
            try:
                if not letter.isalpha():
                    raise TypeError('Lo siento, solo se pueden introducir carácteres')
            except TypeError as isNotString:
                print(isNotString)
            else:
                coin = 0
                for i in range(0, lenghtWord):
                    if mistakes == 5:
                            print(HANGMAN_IMAGES[mistakes+1])
                            print(f'¡Perdiste! Otra vez será.')
                            return False
                    else:
                        if letter == word[i]:
                            hiddenWord[i] = letter
                            coin += 1

                        if hiddenWord.count('_') == 0 and mistakes < 5:
                            print(f'¡Ganaste! La palabra secreta es {word}')
                            return False

                if coin == 0:
                    mistakes += 1
                coin = 0

def run():
    game()


if __name__ == '__main__':
    run()