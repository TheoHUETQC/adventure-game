import random
import pygame
from GameConfig import GameConfig

from player import Player
from map import Map

affichage_pygame = True
affichage_console = not(affichage_pygame)

#generation du Joueur
posPlayerX = 2 #coordonée de base du joueur dans le chunk
posPlayerY = 2
coChunkX = 0 #coordonée du chunk ou se trouve le joueur
coChunkY = 0
player = Player(posPlayerX,posPlayerY, coChunkX, coChunkY)

#generation de la map
if affichage_pygame :
    pygame.init()
    window = pygame.display.set_mode(
        (GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT)
    )
    pygame.display.set_caption("Mon Jeu 2D en Pygame")
else :
    window = 1
chunk = {}
map = Map(window)

GameOver = False
while not(GameOver) : #commence la partie
    
    map.updateMap(player.coChunkXY[0],player.coChunkXY[1], chunk) #centre la map autour du joueur

    if affichage_pygame :
        map.affichagePygame(player)
    if affichage_console :
        map.affichageConsole(player)

    ###### joueur interagie ######
    pressed_keys = input("appuie sur une touche : ") #demande une input au joueur
    listPressed_keys = list(pressed_keys)
    NbrDaction = len(listPressed_keys)
    if len(listPressed_keys) > GameConfig.MAXCOMBO : #pour eviter que le joueur puisse faire plus de 7 actions
        NbrDaction = GameConfig.MAXCOMBO
    for n in range(NbrDaction) : #pour effectuer plusieur action
        if pressed_keys == "a" : #quitte le jeu
            GameOver = True
            break
        player.update(chunk, listPressed_keys[n])
    
