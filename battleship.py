#Gary Li
#12/14/17
#battleship.py

from ggame import* 
from random import randint

Miss = 1
Hit = 2
Ships = 3
radius = 40

def buildBoard(): #creates a 5x5 empty matrix
    return [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]


def redrawAll(): #creates the game board (both player and computer
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            if data['playerBoard'][row][col] == 'O':
                Sprite(emptyCircle,(radius*2*col+radius, radius*2*row+radius))
            elif data['playerBoard'][row][col] == Miss:
                Sprite(missCircle,(radius*2*col+radius, radius*2*row+radius))
            elif data['playerBoard'][row][col] == Hit:
                Sprite(hitCircle,(radius*2*col+radius, radius*2*row+radius))
            elif data['playerBoard'][row][col] == Ships:
                Sprite(shipCircle,(radius*2*col+radius, radius*2*row+radius))
    for row in range(0,5):
        for col in range(0,5):
            if data['computerBoard'][row][col] == 'O':
                Sprite(emptyCircle,(radius*2*col+radius+500, radius*2*row+radius))
            elif data['computerBoard'][row][col] == Miss:
                Sprite(missCircle,(radius*2*col+radius+500, radius*2*row+radius))
            elif data['computerBoard'][row][col] == Hit:
                Sprite(hitCircle,(radius*2*col+radius+500, radius*2*row+radius))
            elif data['computerBoard'][row][col] == Ships:
                Sprite(shipCircle,(radius*2*col+radius+500, radius*2*row+radius))
    Sprite(textPlayer, (150,400))
    Sprite(textComputer, (625,400))
    if data['computerHits'] == 3:
        print('Hi')
        Sprite(TextAsset('Player wins!!', fill=black,style='bold 40pt Times'), (250,400))
    if data['playerHits'] == 3:
        print('Hi')
        Sprite(TextAsset('Computer wins!!', fill=black,style='bold 40pt Times'), (250,400))
             

def mouseClick(event): #the function that places ships/determines if moves are misses/hits
    if data['endGame'] == False:
        if data["playerShips"] < 3:
            if event.x <= radius*10 and event.y <= radius*10:
                playerRow = event.y//(radius*2)
                playerCol = event.x//(radius*2)
                if data['playerBoard'][playerRow][playerCol] != Ships:
                    data['playerBoard'][playerRow][playerCol] = Ships                    
                    data['playerShips'] += 1
                redrawAll()
        elif event.x >= 500 and event.x <= 500+(radius*10):
            playershotRow = event.y//(radius*2)
            playershotCol = (event.x-500)//(radius*2)
            if data['computerBoard'][playershotRow][playershotCol] == Ships:
                    data['computerBoard'][playershotRow][playershotCol] = Hit
                    data['computerHits'] += 1
                    if data['computerHits'] == 3:
                        data['endGame'] = True
                        print('Hello')
                    else:
                        computerTurn()
                    redrawAll()
            elif data['computerBoard'][playershotRow][playershotCol] == 'O':
                    data['computerBoard'][playershotRow][playershotCol] = Miss
                    computerTurn()
                    redrawAll()
    
def computerShips(): #computer places ships in random location on the computer board
    computerShips = 0
    while computerShips < 3:
        computerRow = randint(0,4)
        computerCol = randint(0,4)
        if data['computerBoard'][computerRow][computerCol] != Ships:
            data['computerBoard'][computerRow][computerCol] = Ships
            computerShips += 1

def computerTurn(): #computer takes turn (makes move selecting a random location on the player board to fire its shot)
    playerRow = randint(0,4)
    playerCol = randint(0,4)
    if data['playerBoard'][playerRow][playerCol] == Ships:
        data['playerBoard'][playerRow][playerCol] = Hit
        data['playerHits'] += 1
        if data['playerHits'] == 3:
            data['endGame'] = True
            print('Hello')
        redrawAll()
    elif data['playerBoard'][playerRow][playerCol] == 'O':
        data['playerBoard'][playerRow][playerCol] = Miss
        redrawAll()
    else:
        computerTurn()


if __name__ == '__main__': #sets up/runs the game
    data = {}
    data['playerShips'] = 0
    data['playerShots'] = 0
    data['computerHits'] = 0
    data['playerHits'] = 0
    data['endGame'] = False
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    blue = Color(0x009AFF, 1)
    red = Color(0xBD1D1D,1)
    grey = Color(0x808080,1)
    
    blackLine = LineStyle(1,black)
    
    data['playerBoard'] = buildBoard()
    data['computerBoard'] = buildBoard()
    
    emptyCircle = CircleAsset(radius, blackLine,white)
    missCircle = CircleAsset(radius, blackLine, blue)
    hitCircle = CircleAsset(radius, blackLine,red)
    shipCircle = CircleAsset(radius, blackLine, grey)
    textPlayer = TextAsset('Player', fill=black,style='bold 30pt Times')
    textPlayerWins = TextAsset('Player wins!!', fill=black,style='bold 40pt Times')
    textComputer = TextAsset('Computer', fill=black,style='bold 30pt Times')
    textComputerWins = TextAsset('Computer wins!!', fill=black,style='bold 40pt Times')

    redrawAll()
    App().listenMouseEvent("click", mouseClick)
    computerShips()
    App().run()