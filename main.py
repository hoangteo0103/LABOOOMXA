from List_Modunle import *
import Main_Menu_Window
from pygame import mixer

mixer.init()

mixer.music.load("Game_Data/Sound/Your_Smile.mp3")

mixer.music.set_volume(0.5)

mixer.music.play(-1)

Main_Menu_Window.Run()