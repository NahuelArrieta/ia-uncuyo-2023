import random
from enum import Enum

class Action(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    CLEAN = "CLEAN"
    IDLE = "IDLE"

class Enviroment: 
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.chart = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
        # chart[i][j] = 0 --> clean, 1 --> dirty

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.init_posX = init_posX
        self.init_posY = init_posY
        

        # Fill chart:
        for i in range(sizeX):
            for j in range(sizeY):
                prob = random.random()
                if prob < dirt_rate:
                    self.chart[i][j] = 1

    def validate_pos(self, posX, posY):
        if posX >= 0 and posX < self.sizeX:
            if posY >= 0 and posY < self.sizeY:
                return True
        return False
    
    def is_dirty(self, posX, posY):
        return self.chart[posX][posY] == 1
    
    def clean_slot(self, posX, posY):
        self.chart[posX][posY] = 0
    