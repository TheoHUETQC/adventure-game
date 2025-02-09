import random
from GameConfig import GameConfig

from chunk import Chunk

class Map :
    def __init__(self) :
        self.map = []
    
    def affichage(self, player) :
        for y in range(int(len(self.map)*(GameConfig.RESOLUTION-1)/2.4),int(len(self.map) - (len(self.map)*(GameConfig.RESOLUTION-1)/2.4))) : #parcours la map pour l AFFICHAGE resolution 10/6
            for x in range(len(self.map[y])) :
                if (x == player.xy[0]+GameConfig.NBR*GameConfig.CHAMPS_DE_VISION) and (y == player.xy[1]+GameConfig.NBR*GameConfig.CHAMPS_DE_VISION) :
                    print("👼",end = "")
                elif self.map[y][x] == 0 :
                    print("🟩",end = "")
                elif self.map[y][x] == 1 :
                    print("🌳", end = "")
                elif self.map[y][x] == 2 :
                    print("⬛",end = "")
                elif self.map[y][x] == 3 :
                    print("🟫",end = "")
                elif self.map[y][x] == 4 :
                    print("🧰",end = "")
                elif self.map[y][x] == 5 :
                    print("🏠",end = "")
                elif self.map[y][x] == 6 :
                    print("🟦",end = "")
                else : #texture d erreur
                    print("🟪", end = "")
            print("")
        
    def updateMap(self, coChunkX,coChunkY, chunk) : #update la map autour du chunk de coordonée (coChunkX,coChunkY)
        self.map = [] #reset la map
        j = - GameConfig.CHAMPS_DE_VISION #co du chunk en haut a gauche cest i j
        for y in range(GameConfig.NBR*(GameConfig.CHAMPS_DE_VISION*2 + 1)) : #parcours la map pour la REFRESH
            self.map.append([])
            i = - GameConfig.CHAMPS_DE_VISION
            if y%GameConfig.NBR == 0 and y!=0 : #permet de changer de chunk
                j += 1
            for x in range(GameConfig.NBR*(GameConfig.CHAMPS_DE_VISION*2 + 1)) :
                if x%GameConfig.NBR == 0 and x!=0 : #permet de changer de chunk
                    i += 1
                if not((str(coChunkX + i)+str(coChunkY + j)) in chunk.keys()) : #verifie si le chunk existe dans le dictionnaire chunk
                    chunk[str(coChunkX + i)+str(coChunkY + j)] = Chunk(coChunkX + i, coChunkY + j) #si non genere le chunk
                self.map[y].append(chunk[str(coChunkX + i)+str(coChunkY + j)].chunk[y - GameConfig.NBR*(j+GameConfig.CHAMPS_DE_VISION)][x - GameConfig.NBR*(i+GameConfig.CHAMPS_DE_VISION)]) #rempli la map par les chunk dans le champs de vision du joueur
        return self.map