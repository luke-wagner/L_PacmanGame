class Sprite:
    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
        self.origin = [0,0] # Default, anchor sprite position at top left
        self.pixelData = [] # Start with an empty list

        for i in range(_width):
            column = ['  '] * _height
            self.pixelData.append(column)

backgroundSprite = Sprite(20, 14)
backgroundSprite.pixelData = [
    ['2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '2D', '2D', '2D', '  ', '  ', '2D', '2D', '2D', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '2D', '  ', '  ', '  ', '  ', '  ', '  ', '2D', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '2D', '  ', '  ', '  ', '  ', '  ', '  ', '2D', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '2D', '2D', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '2D', '2D', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '2D', '2D', '2D', '  ', '  ', '2D', '2D', '  ', '  ', '2D', '2D', '2D', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '2D', '2D', '2D', '  ', '  ', '2D', '2D', '  ', '  ', '2D', '2D', '2D', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '2D', '2D', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '2D', '2D', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '2D', '  ', '  ', '  ', '  ', '  ', '  ', '2D', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '2D', '  ', '  ', '  ', '  ', '  ', '  ', '2D', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '2D', '2D', '2D', '  ', '  ', '2D', '2D', '2D', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '2D'],
    ['2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D', '2D']
]

playerSprite = Sprite(2, 2)
playerSprite.pixelData = [
    ['0B', '0B'],
    ['0B', '0B']
]

pelletSprite = Sprite(1, 1)
pelletSprite.pixelData = [
    ['FF']
]

enemySprite1 = Sprite(2, 2)
enemySprite1.pixelData = [
    ['55', '55'],
    ['55', '55']
]

enemySprite2 = Sprite(2, 2)
enemySprite2.pixelData = [
    ['91', '91'],
    ['91', '91']
]