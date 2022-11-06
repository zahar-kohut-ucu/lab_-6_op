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

print(generate_grid())
