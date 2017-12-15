#Gary Li
#12/14/17
#battleship.py

from ggame import* 
from random import randint

EMPTY = 0
MISS = 1
ROWS = 5
COLS = 5


def buildBoard():
    return [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]
    
buildBoard()


def redrawAll:
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            print(board[row][col],' ',end = '')
        
if __name__ == '__main__': 


App().run()