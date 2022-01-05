from List_Modunle import *

class Play_Board():
	Image = []
	Board = [[-1 for i in range(20)] for j in range(20)]

	def __init__(self, Map_State):
		for i in range(3):
			Path = "Game_Data/Image/Map_" + str(Map_State) + "/tile_" + str(i) + ".png"
			Image_tmp = pygame.image.load(Path)
			Image_tmp = pygame.transform.scale(Image_tmp, (Cell_Width, Cell_Height))
			self.Image.append(Image_tmp)

		Path = "Game_Data/Image/Map_" + str(Map_State) + "/Map.txt"
		Board_File = open(Path)
		Str = Board_File.read()

		for t in range(0, len(Str)):
			x = t // 18
			y = t % 18
			if y == 17: continue
			self.Board[x][y] = int(Str[t])

	def Print_Board(self):
		for i in range(0, 15):
			for j in range(0, 17):
				print(self.Board[i][j], end = ' ')
			print()

	def Draw_Board(self, screen):
		for i in range(15):
			for j in range(17):
				screen.blit(self.Image[0], (264 + j * Cell_Width, i * Cell_Height))
				screen.blit(self.Image[self.Board[i][j]], (264 + j * Cell_Width, i * Cell_Height))

