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
            Sprite(emptyCircle,(RADIUS*2*row+RADIUS, RADIUS*2*col+RADIUS))

def mouseClick(event):
    print(event.x,event.y)
    
        
if __name__ == '__main__':
    data = {}
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    blue = Color(0x009AFF, 1)
    red = Color(0xBD1D1D,1)
    
    blackLine = LineStyle(1,black)
    
    playerBoard = buildBoard()
    computerBoard = buildBoard()
    
    emptyCircle = CircleAsset(radius, blackLine,white)
    missCircle = CircleAsset(radius, blackLine, blue)
    hitCircle = CircleAsset(radius, blackLine,red)
    
    redrawAll()

    App().listenMouseEvent("click", mouseClick)
    App().run()