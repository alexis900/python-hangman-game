from dataclasses import replace
from random import randint
import os
import platform
from typing import Type

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
    lenghtWord = len(word)
    hiddenWord = ['_'] * lenghtWord 
    while True:
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
                for i in range(0, lenghtWord):
                    if letter == word[i]:
                        hiddenWord[i] = letter
                    if hiddenWord.count('_') == 0:
                        print(f'¡Ganaste! La palabra secreta es {word}')
                        return False
            

def run():
    game()


if __name__ == '__main__':
    run()