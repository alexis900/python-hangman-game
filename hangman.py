from dataclasses import replace
from random import randint


def normaliceWord(word):
    replacements = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u' }
    for a, b in replacements.items():
        word = word.replace(a, b).replace('\n', '').upper()
    return word


def readFile():
    with open('./data.txt', 'r', encoding='utf-8') as f:
        words = []
        for lines in f:
            words.append(normaliceWord(lines))

        f.close()
        return words

def selectWord():
    words = readFile()
    randNum = randint(1, len(words))
    return words[randNum]
    

def game():
    word = selectWord()
    while True:
        print(word)
        return False
    


def run():
    game()


if __name__ == '__main__':
    run()