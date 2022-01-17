from PIL import Image
import pygame

# Crop Image

for i in range(61):
	origin_image_path = f'Game_Data/Image/spawn_effect/spawn_effect-{i}.png'
	save_image_path = f'Game_Data/Image/spawn_effect/effect-{i}.png'

	origin_image = Image.open(origin_image_path)

	left = 170
	top = 115
	right = 500
	bottom = 350

	save_image = origin_image.crop((left, top, right, bottom))
	save_image.save(save_image_path)

# Shows the image in image viewer
# save_image.show()

# save_image.save(save_image_path)
