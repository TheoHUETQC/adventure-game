import random
from GameConfig import GameConfig
from entity import Chest
from entity import Tree

class Chunk : 
    def __init__(self, x, y) :
        self.xy = [x, y]
        self.entityIn = {}
        proba = int(random.randint(0, 6)) #choisis quel type de chunk generer # int(abs(x-y*x*SEED)) % 100 // 10 
        if self.xy == [0,0] :
            self.chunkForet()
        elif proba == 1 :
           self.chunkMaison()
        elif proba == 2 :
            self.chunkWater()
        else:
            self.chunkForet()

    def chunkForet(self) : #genere un chunk type arbre
        self.chunk = []
        arbre = 100
        maison = 0
        for y in range(GameConfig.NBR) :
            ligne = []
            for x in range(GameConfig.NBR) :
                proba = int(random.randint(maison, arbre))
                if proba >= 90 :
                    ligne.append(1)
                    self.entityIn["tree" + str(x) + str(y)] = Tree(x, y, self.xy[0], self.xy[1])
                    arbre += -10
                elif proba < 1 :
                    maison = 1
                    ligne.append(5)
                else :
                    ligne.append(0)
            self.chunk.append(ligne)
        """ version avec seed
        self.chunk = []
        for i in range(GameConfig.NBR) :
            self.chunk.append([])
            for j in range(GameConfig.NBR) :
                self.chunk[i].append(0)
        
        i, nbr_darbre = 0 , 5
        while nbr_darbre >= 4 :
            i += 1
            nbr_darbre = int(abs((GameConfig.SEED+i*10)-self.xy[0]*self.xy[1]-self.xy[0])) % 100 // 10
        for i in range(nbr_darbre) :
            x_arbre = int(abs(GameConfig.SEED*(self.xy[0]+self.xy[1]*self.xy[1]+i))) % 100 // 10
            y_arbre = int(abs(GameConfig.SEED*(self.xy[1]-self.xy[0]*self.xy[0]*i))) % 100 // 10
            while x_arbre >= GameConfig.NBR : x_arbre += - GameConfig.NBR
            while y_arbre >= GameConfig.NBR : y_arbre += - GameConfig.NBR
            self.chunk[y_arbre][x_arbre] = 1
        if nbr_darbre <= 2 :
            x_maison = int(abs(GameConfig.SEED-self.xy[0]+self.xy[0]+self.xy[1]*i)) % 100 // 10
            y_maison = int(abs(GameConfig.SEED+self.xy[1]+self.xy[1]*self.xy[0]-i)) % 100 // 10
            while x_maison >= GameConfig.NBR : x_maison += - GameConfig.NBR
            while y_maison >= GameConfig.NBR : y_maison += - GameConfig.NBR
            self.chunk[y_maison][x_maison] = 1
        """
            
    def chunkMaison(self) : #genere un chunk type maison
        maison = 100
        proba = int(random.randint(0, maison))
        if proba >= 50 :
            self.entityIn["chest" + str(3) + str(1)] = Chest(3, 1, self.xy[0], self.xy[1])
            self.chunk = [[0,2,2,2,2],
                          [0,2,3,4,2],
                          [0,2,3,3,2],
                          [0,2,3,2,2],
                          [0,0,0,0,0]]
        else :
            self.entityIn["chest" + str(1) + str(2)] = Chest(1, 2, self.xy[0], self.xy[1])
            self.chunk = [[2,2,2,2,2],
                          [2,3,3,3,2],
                          [2,4,3,3,3],
                          [2,3,3,3,2],
                          [2,2,2,2,2]]

    def chunkWater(self) : #genere un chunk type marre
        self.chunk = []
        for j in range(GameConfig.NBR) :
            self.chunk.append([])
            for i in range(GameConfig.NBR) :
                if i == 0 or i == 4 or j == 0 or j == 4 :
                    self.chunk[j].append(0)
                elif i == 2 and j == 2 :
                    self.chunk[j].append(6)
                else :
                    if self.chunk[j-1][i-1] != 0 or self.chunk[j-1][i] != 0 or self.chunk[j][i-1] or self.chunk[j-1][i+1] != 0 :
                        proba = random.randint(1, random.randint(3, 6))
                    else :
                        proba = random.randint(1, random.randint(2, 4))
                    if proba == 1 :
                        self.chunk[j].append(0)
                    else :
                        self.chunk[j].append(6)
