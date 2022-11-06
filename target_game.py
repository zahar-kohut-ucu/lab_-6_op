'''Target game (English)'''
from typing import List
import random
import string
alph_low = list(string.ascii_uppercase)
alph_up = list(string.ascii_uppercase)


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    board = []
    for _b in range(3):
        line = []
        for _d in range(3):
            line.append(random.choice(alph_up))
        board.append(line)
    return board



def get_words(_f: str, letters: List[str]) -> List[str]:
    """
    Reads the file _f. Checks the words with rules and returns a list of words.
    """
    right_words = []
    with open(_f, 'r', encoding='utf-8') as _en:
        content = _en.readlines()[6:]
        for word in content:
            word = word.strip().lower()
            if  len(word.strip())>3 and letters[4] in word:
                if all(_u in letters and word.count(_u) <= letters.count(_u) for _u in word):
                    right_words.append(word)
    return right_words

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_words = []
    while True:
        try:
            user_words.append(input())
        except EOFError:
            break
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str]\
    , words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_words = []
    for word in user_words:
        if not word in words_from_dict:
            if  len(word.strip())>3 and letters[4] in word:
                word = word.strip().lower()
                if all(_u in letters and word.count(_u) <= letters.count(_u) for _u in word):
                    pure_words.append(word)
    return pure_words


def results(user_ans, letters):
    '''
    Prints and write into files results of game.
    '''
    all_words = get_words('en.txt', letters)
    pure_words = get_pure_user_words(user_ans, letters, all_words)
    missed_words = []
    for word1 in all_words:
        if not word1 in user_ans:
            missed_words.append(word1)
    right_ans = 0
    for word2 in user_ans:
        if word2 in all_words:
            right_ans += 1
    result = [str(right_ans), ', '.join(all_words), ', '.join(missed_words), ', '.join(pure_words)]
    print('\n'.join(result))
    with open('result.txt', 'w', encoding='utf-8') as res:
        res.write('\n'.join(result))



def grid_into_letters(grid):
    '''
    Transfrom grid into 'letters' argument.
    '''
    for _i, item in enumerate(grid):
        grid[_i] = ''.join(item)
    grid = list(''.join(grid).lower())
    return grid
