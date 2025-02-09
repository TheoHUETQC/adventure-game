import random
from GameConfig import GameConfig
from entity import Entity

class Player(Entity) :
    def update(self, chunk, pressed_keys) :
        if (pressed_keys == "z") and (self.pasObstacle("up", chunk)) : #deplace en haut
            self.xy[1] += -1
        elif (pressed_keys == "s") and (self.pasObstacle("down", chunk)) : #deplace en bas
            self.xy[1] += 1
        elif (pressed_keys == "d") and (self.pasObstacle("right", chunk)) : #deplace a droite
            self.xy[0] += 1
        elif (pressed_keys == "q") and (self.pasObstacle("left", chunk)) : #deplace a gauche
            self.xy[0] += -1
        
        ###### si joueur change de chunk ######
        if self.xy[1] < 0 : #haut
            self.xy[1] = GameConfig.NBR - 1
            self.coChunkXY[1] += -1
        elif self.xy[1] >= GameConfig.NBR : #bas
            self.xy[1] = 0
            self.coChunkXY[1] += 1
        elif self.xy[0] >= GameConfig.NBR : #droite
            self.xy[0] = 0
            self.coChunkXY[0] += 1
        elif self.xy[0] < 0 : #gauche
            self.xy[0] = GameConfig.NBR - 1
            self.coChunkXY[0] += -1
        
        if pressed_keys == "e" : #interagie
            if len(chunk[str(self.coChunkXY[0]) + str(self.coChunkXY[1])].entityIn) != 0 : #verifie qu il y est des entités dans le chunk du joueur  
                for y in range(-1,2) : #regarde les alentours du joueur
                    for x in range(-1,2) :
                        [i,j] = self.co_chunk([self.xy[0]+x, self.xy[1]+y]) #permet de connaitre le chunk ou se trouve la modification
                        if chunk[str(self.coChunkXY[0] + i)+str(self.coChunkXY[1] + j)].chunk[(self.xy[1]+y) - GameConfig.NBR*(j+1)][(self.xy[0]+x) - GameConfig.NBR*(i+1)] == 4 : #verifie si il y a un coffre                            
                            self.inventory.append(GameConfig.ITEM[int(random.randint(0, GameConfig.NBRDITEM-1))]) #ajoute l item dans l inventaire
                            chunk[str(self.coChunkXY[0] + i)+str(self.coChunkXY[1] + j)].chunk[(self.xy[1]+y) - GameConfig.NBR*(j+1)][(self.xy[0]+x) - GameConfig.NBR*(i+1)] = 3 #retire le coffre
                            break
                        elif chunk[str(self.coChunkXY[0] + i)+str(self.coChunkXY[1] + j)].chunk[(self.xy[1]+y) - GameConfig.NBR*(j+1)][(self.xy[0]+x) - GameConfig.NBR*(i+1)] == 1 : #verifie si il y a un arbre 
                            self.inventory.append("bois") #ajoute l item dans l inventaire 
                            chunk[str(self.coChunkXY[0] + i)+str(self.coChunkXY[1] + j)].chunk[(self.xy[1]+y) - GameConfig.NBR*(j+1)][(self.xy[0]+x) - GameConfig.NBR*(i+1)] = 0 #retire l'arbre
                            break
                    else :
                        continue
                    break
        elif pressed_keys == "f" : #donne coordonné du joueur
            print(f"vous etes en x = {self.coChunkXY[0]*GameConfig.NBR + self.xy[0]}, y = {self.coChunkXY[1]*GameConfig.NBR + self.xy[1]} dans le chunk {self.coChunkXY} en {self.xy}")
        elif pressed_keys == "i" : #ouvre l invetaire
            print(self.inventory)