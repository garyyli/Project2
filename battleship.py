#Gary Li
#12/14/17
#battleship.py

from random import randint
board = [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]

def buildBoard1():
    for row in range(0,5):
        for col in range(0,5):
            print(board[row][col],' ',end = '')
        print()

buildBoard1()


def redrawAll:
    for item in App().spritelist[:]:
        item.destroy()
