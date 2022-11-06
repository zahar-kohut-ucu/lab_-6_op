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
            line.append(alph_up[random.randrange(26)])
        board.append(line)
    return board



def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    right_words = []
    with open(f, 'r', encoding='utf-8') as en:
        content = en.readlines()[6:]
        for word in content:
            if  len(word.strip())>3 and letters[4] in word:
                word = word.strip().lower()
                t_word = list(set([(_h, word.count(_h)) for _h in word]))
                for _u in t_word:
                    if _u[0] in letters and _u[1] <= letters.count(_u[0]):
                        right_words.append(word)
    return right_words

print(get_words('en.txt',  ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']))

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


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
