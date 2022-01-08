from math import *
from CONST import *

class Item:
	def __init__(self, X, Y, image):
		self.X = X;
		self.Y = Y;
		self.image = Item_Image[0]

	def Draw(self, Screen) :
		Row = self.X * 48 + 264
		Col = self.Y * 48

		Screen.blit(self.image, (Row, Col))