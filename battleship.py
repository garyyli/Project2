#Gary Li
#12/14/17
#battleship.py

from ggame import* 
from random import randint

radius = 40

def buildBoard():
    return [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]
    
buildBoard()


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            Sprite(emptyCircle,(radius*2*row+radius, radius*2*col+radius))
    for row in range(0,5):
        for col in range(0,5):
            Sprite(emptyCircle,(radius*2*row+radius+300, radius*2*col+radius+300))
            

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