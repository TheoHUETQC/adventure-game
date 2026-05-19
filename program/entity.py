import random
from GameConfig import GameConfig

class Entity :
    def __init__(self, x, y, coChunkX, coChunkY) :
        self.xy = [x, y]
        self.coChunkXY = [coChunkX, coChunkY]
        self.inventory = []
    
    def co_chunk(self, xy) : #donne les coordonné du chunk ou se trouve la case xy 
        x, y = xy[0], xy[1]

        x_in_chunk = x%(GameConfig.NBR)
        chunk_x = (x - x_in_chunk)//GameConfig.NBR

        y_in_chunk = y%(GameConfig.NBR)
        chunk_y = (y - y_in_chunk)//GameConfig.NBR
        print(f"x, y={xy}, chunk={[int(chunk_x), int(chunk_y)]}")
        return [int(chunk_x), int(chunk_y)]
             
    def pasObstacle(self, mvt, chunk) : # renvoie True si la case où l'entité veut se deplacer est un sol
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
        if newY < 0 :
            newY = GameConfig.NBR - GameConfig.speed
            newChunkY += -1
        if newY >= GameConfig.NBR :
            newY = 0
            newChunkY += 1
        if newX < 0 :
            newX = GameConfig.NBR - GameConfig.speed
            newChunkX += -1
        if newX >= GameConfig.NBR :
            newX = 0
            newChunkX += 1
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
