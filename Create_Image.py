from PIL import Image
import pygame

# Crop Image
origin_image_path = 'Game_Data/Image/Skin_7.png'
save_image_path = 'Test.png'

origin_image = Image.open(origin_image_path)

left = 160
top = 0
right = 480
bottom = 330

save_image = origin_image.crop((left, top, right, bottom))

# Shows the image in image viewer
save_image.show()

# save_image.save(save_image_path)
