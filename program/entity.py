import random
from GameConfig import GameConfig

class Entity :
    def __init__(self, x, y, coChunkX, coChunkY) :
        self.xy = [x, y]
        self.coChunkXY = [coChunkX, coChunkY]
        self.inventory = []
    
    def co_chunk(self, xy) : #donne les coordonné du chunk ou se trouve la case xy 
        i, j = 0 , 0
        if (xy[0] <= 4) :
            i = -1
        elif (xy[0] >= 10) :
            i = 1
        if (xy[1] <= 4) :
            j = -1
        elif (xy[1] >= 10) :
            j = 1
        return [i,j]
             
    def pasObstacle(self, mvt, chunk) : # renvoie True si la case ou l'entité veut se deplacer est un sol
        newX, newY = self.xy[0], self.xy[1]
        newChunkX, newChunkY = self.coChunkXY[0], self.coChunkXY[1]
        if self.xy[1] == 0 and mvt == "up" : #cas particulier de changement de chunk
            newY = GameConfig.NBR - GameConfig.speed
            newChunkY += -1
        elif self.xy[1] == GameConfig.NBR-GameConfig.speed and mvt == "down" : 
            newY = 0
            newChunkY += 1 
        elif self.xy[0] == GameConfig.NBR-GameConfig.speed and mvt == "right" : 
            newX = 0
            newChunkX += 1
        elif self.xy[0] == 0 and mvt == "left" :
            newX = GameConfig.NBR - GameConfig.speed
            newChunkX += -1
        else : #si il n y a pas de changement de chunk
            if mvt == "up" :
                newY += -GameConfig.speed
            elif mvt == "down" :
                newY += GameConfig.speed
            elif mvt == "right" :
                newX += GameConfig.speed
            else : # mvt == "left" :
                newX += -GameConfig.speed
        return chunk[str(newChunkX)+ str(newChunkY)].chunk[int(newY)][int(newX)] in GameConfig.FLOOR

class Object(Entity) :
    def destroy(self) : #laisse ce qu il y a dans son inventaire par terre
        pass
    def aCoterDuJoueur(self,coJoueur) :
        pass

class Chest(Object) :
    def __init__(self, x, y, coChunkX, coChunkY):
        super().__init__(x, y, coChunkX, coChunkY)
        self.inventory.append(GameConfig.ITEM[int(random.randint(0, GameConfig.NBRDITEM-1))])
    def destroy(self):
        super().destroy()#reutilise la fonction destroy de object
    
class Tree(Object) :
    def __init__(self, x, y, coChunkX, coChunkY):
        super().__init__(x, y, coChunkX, coChunkY)
        self.inventory.append("wood")
    def destroy(self) :
        super().destroy()#reutilise la fonction destroy de object       
    def burn(self) :
        pass
