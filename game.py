import copy
import asyncio
from pynput import keyboard
from pynput.keyboard import Key

from LightsController import LightsController
from sprites import *

class GameObject:
    def __init__(self, _name, _sprite=None, _position=[0,0]):
        self.name = _name
        self.sprite = _sprite
        self.position = _position
        self.zIndex = 0  # Default value

GAME_WIDTH = 20
GAME_HEIGHT = 14

drawingFrame = False

lightsController = LightsController()

previousFrame = []
currentFrame = []
gameObjects = []

for i in range(GAME_WIDTH):
    column = ['  '] * GAME_HEIGHT
    currentFrame.append(column)
    previousFrame.append(column.copy()) # must use copy to ensure same column is not used for both matrices

backgroundObj = GameObject("background", backgroundSprite)
gameObjects.append(backgroundObj)

playerObj = GameObject("player", playerSprite, [9,6])
gameObjects.append(playerObj)

def clearFrame():
    global currentFrame
    
    for i in range(GAME_WIDTH):
        for j in range(GAME_HEIGHT):
            currentFrame[i][j] = '  '

def newFrame():
    global drawingFrame
    global currentFrame
    global previousFrame

    drawingFrame = True

    clearFrame()

    # Sort the gameObjects list by zIndex so sprites are drawn in the correct order
    # Not sure if this will work
    gameObjects.sort(key=lambda obj: obj.zIndex)

    for object in gameObjects:
        drawGameObject(object)

    asyncio.run(lightsController.drawFramePartial(currentFrame, previousFrame))

    previousFrame = copy.deepcopy(currentFrame)

    drawingFrame = False

def drawGameObject(gameObject):
    if gameObject.sprite == None:
        print("ERROR: Draw function called on object with no sprite")
        return

    for i in range(gameObject.sprite.width):
        for j in range(gameObject.sprite.height):
            # Draw pixel
            coordX = i + gameObject.position[0] - gameObject.sprite.origin[0]
            coordY = j + gameObject.position[1] - gameObject.sprite.origin[1]
            ledNumber = coordX * 20 + coordY
            color = gameObject.sprite.pixelData[i][j]
            
            if coordX >= 0 and coordX < GAME_WIDTH and coordY >= 0 and coordY < GAME_HEIGHT:
                #print("Coloring (" + str(coordX) + ", " + str(coordY) + "), led number: " + str(ledNumber) + ", with " + color)
                currentFrame[coordX][coordY] = color

#asyncio.run(lightsController.drawBlankFrame())

#newFrame()

def on_press(key):
    if drawingFrame:
        return

    if key == Key.up:
        playerObj.position[1] -= 1
        newFrame()
    elif key == Key.down:
        playerObj.position[1] += 1
        newFrame()
    elif key == Key.right:
        playerObj.position[0] += 1
        newFrame()
    elif key == Key.left:
        playerObj.position[0] -= 1
        newFrame()


# Create a listener and start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

while True:
    continue
    
# Disconnect from the lights
asyncio.run(lightsController.disconnect())