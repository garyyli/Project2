#Gary Li
#12/14/17
#battleship.py

from ggame import* 
from random import randint

radius = 50

def buildBoard():
    return [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]
    
buildBoard()


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            print(board[row][col],' ',end = '')
        
if __name__ == '__main__':
    data = {}
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000,1)
    
    playerBoard = buildBoard()
    computerBoard = buildBoard()
    
    emptyCircle = CircleAsset(radius,LineStyle(1,black),white)
    missCircle = CircleAsset(radius,LineStyle(1,black), blue)
    hitCircle = CircleAsset(radius,LineStyle(1,black),red)
    
    
    App().run()