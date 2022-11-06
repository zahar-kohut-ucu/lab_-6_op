'''Target game (Ukrainian)'''
import random

def generate_grid():
    '''
    Generates list of letters - i.e. grid for the game.
    e.g. ['е', 'п', 'в', 'о', 'є']
    '''
    ukr_alph = list('абвгґдеєжзиіїйклмнопрстуфхцчшщюя')
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

def get_words(_f, letters):
    '''
    Return list of tuples (pairs - (word, part_of_speech)) with length less than 6
    and starting with a letter from 'letters' list.
    '''
