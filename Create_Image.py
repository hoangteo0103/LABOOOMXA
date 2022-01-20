from PIL import Image
import pygame

# Crop an Image
def Crop_an_Image():
	origin_image_path = f'Game_Data/Image/item/test.jpg'
	save_image_path = f'Game_Data/Image/item/test.png'

	origin_image = Image.open(origin_image_path)

	Row = 220
	Col = 93

	left = 15
	top = 20
	right = 205
	bottom = 93

	for i in range(6):
		save_image = origin_image.crop((Row * i + left, top, Row * i + right, bottom))
		save_image.show()
	# save_image.save(save_image_path)

# Crop more images
def Crop_many_Images():
	for i in range(7):
		origin_image_path = f'Game_Data/Image/item/Item_4.png'
		save_image_path = f'Game_Data/Image/item/Yasuo-{i}.png'

		origin_image = Image.open(origin_image_path)

		Row = 220
		Col = 93

		left = 15
		top = 20
		right = 205
		bottom = 93

		save_image = origin_image.crop((Row * i + left, top, Row * i + right, bottom))
		# save_image.show()
		save_image.save(save_image_path)

# Crop_an_Image()

Crop_many_Images()
