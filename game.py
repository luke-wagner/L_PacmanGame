import copy
import asyncio

from LightsController import LightsController

class GameObject:
    def __init__(self, _name, _sprite=None, _position=[0,0]):
        self.name = _name
        self.sprite = _sprite
        self.position = _position
        self.zIndex = 0  # Default value

class Sprite:
    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
        self.origin = [0,0] # Default, anchor sprite position at top left
        self.pixelData = [] # Start with an empty list

        for i in range(_width):
            column = [' '] * _height
            self.pixelData.append(column)

GAME_WIDTH = 20
GAME_HEIGHT = 14

lightsController = LightsController()

backgroundSprite = Sprite(20, 14)
backgroundSprite.pixelData = [
    ['2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', '2D', '2D', '2D', 'FE', 'FE', '2D', '2D', '2D', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', '2D', '2D', '2D', 'FE', 'FE', '2D', '2D', 'FE', 'FE', '2D', '2D', '2D', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', '2D', '2D', '2D', 'FE', 'FE', '2D', '2D', 'FE', 'FE', '2D', '2D', '2D', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', '2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', '2D', '2D', '2D', 'FE', 'FE', '2D', '2D', '2D', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', 'FE', '2D'],
    ['2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D']
]

previousFrame = []
currentFrame = []
gameObjects = []

for i in range(GAME_WIDTH):
    column = [' '] * GAME_HEIGHT
    currentFrame.append(column)
    previousFrame.append(column.copy()) # must use copy to ensure same column is not used for both matrices

backgroundObj = GameObject("background", backgroundSprite)
gameObjects.append(backgroundObj)

def clearFrame():
    global currentFrame
    
    for i in range(GAME_WIDTH):
        for j in range(GAME_HEIGHT):
            currentFrame[i][j] = ' '

def newFrame():
    global currentFrame
    global previousFrame

    clearFrame()

    # Sort the gameObjects list by zIndex so sprites are drawn in the correct order
    # Not sure if this will work
    gameObjects.sort(key=lambda obj: obj.zIndex)

    for object in gameObjects:
        drawGameObject(object)

    asyncio.run(lightsController.drawFramePartial(currentFrame, previousFrame))

    previousFrame = copy.deepcopy(currentFrame)

def drawGameObject(gameObject):
    if gameObject.sprite == None:
        print("ERROR: Draw function called on object with no sprite")
        return

    for i in range(gameObject.sprite.width):
        for j in range(gameObject.sprite.height):
            # Draw pixel
            coordX = i + gameObject.position[1] - gameObject.sprite.origin[1]
            coordY = j + gameObject.position[0] - gameObject.sprite.origin[0]
            ledNumber = coordX * 20 + coordY
            color = gameObject.sprite.pixelData[i][j]
            
            if coordX >= 0 and coordX < GAME_WIDTH and coordY >= 0 and coordY < GAME_HEIGHT:
                #print("Coloring (" + str(coordX) + ", " + str(coordY) + "), led number: " + str(ledNumber) + ", with " + color)
                currentFrame[coordX][coordY] = color

newFrame()

backgroundObj.position = [0,1]

newFrame()

# Disconnect from the lights
asyncio.run(lightsController.disconnect())