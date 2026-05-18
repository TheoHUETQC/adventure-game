import pygame
import random
from GameConfig import GameConfig

from chunk import Chunk

class Map :
    def __init__(self,window) :
        self.map = []
        self.window = window
    
    def affichageConsole(self, player) :
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
    
    def affichagePygame(self, player):
        # Couleurs
        BEIGE = (220, 200, 160)
        VERT_POMME = (0, 255, 0)
        VERT_FONCE = (0, 150, 0)
        NOIR = (0, 0, 0)
        MARRON = (120, 70, 15)
        ROUGE = (255, 0, 0)
        ROUGE_FONCE = (150, 0, 0)
        BLEU = (0, 0, 255)
        VIOLET = (180, 0, 180)

        # Taille d’une case à l’écran
        CASE = GameConfig.CASE_SIZE 

        # Efface l’écran
        self.window.fill((0, 0, 0))

        # Parcours de la map
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                # Couleur de la case
                val = self.map[y][x]

                if val == 0:
                    color = VERT_POMME
                elif val == 1:
                    color = VERT_FONCE
                elif val == 2:
                    color = NOIR
                elif val == 3:
                    color = MARRON
                elif val == 4:
                    color = ROUGE
                elif val == 5:
                    color = ROUGE_FONCE
                elif val == 6:
                    color = BLEU
                else:
                    color = VIOLET

                # Vérification du joueur
                """if (x == player.xy[0] + GameConfig.NBR * GameConfig.CHAMPS_DE_VISION) and (y == player.xy[1] + GameConfig.NBR * GameConfig.CHAMPS_DE_VISION):
                    color = BEIGE"""

                # Calcul position d’affichage 
                draw_x = (x - (player.xy[0])+0.5) * CASE
                draw_y = (y - (player.xy[1])+0.5) * CASE - (GameConfig.SCREEN_WIDTH / 4)
                
                # Dessin de la case 
                pygame.draw.rect(self.window, color,
                                (draw_x, draw_y, CASE, CASE))
        # Dessin du joueur 
        center = ((GameConfig.NBR * GameConfig.CHAMPS_DE_VISION) * CASE + CASE/2, (GameConfig.NBR * GameConfig.CHAMPS_DE_VISION) * CASE + CASE/2 - (GameConfig.SCREEN_WIDTH / 4))
        color = BEIGE
        pygame.draw.circle(self.window, color, center, CASE/3)
        """pygame.draw.rect(self.window, color,
                                (draw_x, draw_y, CASE, CASE))"""
        
        # Met l’affichage à jour
        pygame.display.flip()

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