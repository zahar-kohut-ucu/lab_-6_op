'''Target game (Ukrainian)'''
from typing import List
import random

def generate_grid() -> List[str]:
    '''
    Generates list of letters - i.e. grid for the game.
    e.g. ['e', 'п', 'в', 'o', 'є']
    '''
    ukr_alph = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
    board = []
    while len(board) < 5:
        letter = random.choice(ukr_alph)
        if letter not in board:
            board.append(letter)
    return board

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

def get_words(_f: str, letters: List[str]) -> List[tuple[str]]:
    '''
    Return list of tuples (pairs - (word, part_of_speech)) with length less than 6
    and starting with a letter from 'letters' list.
    >>> get_words("base.lst", ['й', 'є', 'ю'])
    [('євнух', 'noun'), ('єврей', 'noun'), ('євро', 'noun'), ('єгер', 'noun'), \
('єдваб', 'noun'), ('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), \
('ємно', 'adverb'), ('єна', 'noun'), ('єнот', 'noun'), ('єпарх', 'noun'), \
('єресь', 'noun'), ('єри', 'noun'), ('єрик', 'noun'), ('єрик', 'noun'), \
('єство', 'noun'), ('єті', 'noun'), ('єхида', 'noun'), ('йняти', 'verb'), \
('йог', 'noun'), ('йога', 'noun'), ('йод', 'noun'), ('йодат', 'noun'), \
('йодид', 'noun'), ('йодил', 'noun'), ('йодит', 'noun'), ('йодль', 'noun'), \
('йола', 'noun'), ('йолоп', 'noun'), ('йомен', 'noun'), ('йон', 'noun'), \
('йорж', 'noun'), ('йорж', 'noun'), ('йот', 'noun'), ('йота', 'noun'), \
('йти', 'verb'), ('йтися', 'verb'), ('юань', 'noun'), ('юга', 'noun'), \
('югурт', 'noun'), ('юда', 'noun'), ('юдей', 'noun'), ('юдин', 'adjective'), \
('юдоль', 'noun'), ('юзом', 'adverb'), ('юїтка', 'noun'), ('юка', 'noun'), \
('юкола', 'noun'), ('юнак', 'noun'), ('юнга', 'noun'), ('юний', 'adjective'), \
('юніор', 'noun'), ('юнка', 'noun'), ('юнкер', 'noun'), ('юнкор', 'noun'), ('юннат', 'noun'), \
('юнь', 'noun'), ('юпка', 'noun'), ('юра', 'noun'), ('юрба', 'noun'), \
('юрик', 'noun'), ('юрист', 'noun'), ('юрма', 'noun'), ('юрода', 'noun'), \
('юрок', 'noun'), ('юрок', 'noun'), ('юрта', 'noun'), ('юрфак', 'noun'), \
('юс', 'noun'), ('ют', 'noun'), ('ютуб', 'noun'), ('юферс', 'noun'), \
('юхта', 'noun'), ('юшити', 'verb'), ('юшка', 'noun'), ('ююба', 'noun')]
    '''
    parts_of_speech_dict = {'/n': 'noun', 'noun': 'noun', '/numr': None, 'adv': 'adverb', \
    'adj': 'adjective', '/adj': 'adjective','/v': 'verb', 'verb': 'verb', 'advp': 'verb'}
    words = []
    with open(_f, 'r', encoding='utf-8') as base:
        content = base.read().split('\n')
        for word in content:
            word = word.lower() + ' '
            if len(word[:word.find(' ')]) <= 5 and word[0] in letters:
                part = None
                for item in parts_of_speech_dict.items():
                    if item[0] in word:
                        part = item[1]
                if part:
                    words.append((word[:word.find(' ')], part))
    return words

def check_user_words(user_words: List[str], language_part: str, \
letters: List[str], dict_of_words: List[str]) -> List[str]:
    '''
    Returns a list of words a user guessed and didn't guess in game of Target.
    '''
    right_words = []
    for item in dict_of_words:
        if item[0][0] in letters and item[1] == language_part:
            right_words.append(item[0])
    right_user_words = [el1 for el1 in user_words if el1 in right_words]
    missed_words = [el2 for el2 in right_words if el2 not in user_words]
    return (right_user_words, missed_words)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
