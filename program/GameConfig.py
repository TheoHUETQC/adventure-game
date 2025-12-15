class GameConfig :
	def __init__(self) :
     ###### parametre dev ######
		self.ITEM = ["Epée","Hache"] #item disponible dans les coffres          
		self.NBRDITEM = len(self.ITEM)
		self.MAXCOMBO = 7 #nombre d action que peut faire en 1 input
		self.NBR = 5 #resolution d un chunk 5x5
		self.FLOOR = [0, 3] #les cases sur les quels le joueur peut marcher
		self.SEED = 156
  
	###### parametre du jeu ######
		self.CHAMPS_DE_VISION = 3 #nombre de chunk qu on voit autour de nous (entier)        
		self.RESOLUTION = 16/9 #resolution de l'ecran 

	###### fenêtre pygame ######
		self.SCREEN_HEIGHT = 800
		self.SCREEN_WIDTH = self.SCREEN_HEIGHT * self.RESOLUTION
		self.CASE_SIZE =  self.SCREEN_WIDTH / (self.NBR * self.CHAMPS_DE_VISION * 2 + 1) # en pixels 
  
GameConfig = GameConfig()
