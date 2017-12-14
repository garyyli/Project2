#Gary Li
#12/14/17
#battleship.py

board = [['O','O','O'],['O','O','O'],['O','O','O']]

def buildBoard():
    for row in range(0,3):
        for col in range(0,3):
            print(board[row][col],' ',end = '')
        print()

buildBoard()

