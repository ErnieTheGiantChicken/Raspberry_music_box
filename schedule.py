import pygame
from schedule_module import *
import time
import random
import os

pygame.mixer.init()
paths = os.listdir('/home/Admin/Music_box/music_folder')
print(len(paths))
special_times = ['9:50','10:55','12:55','14:05']




class music_player():
	def __init__(self,paths):
		self.paths = paths
	
	def end(self):
		pygame.mixer.music.fadeout(1000)
		pygame.mixer.music.stop()
		pygame.mixer.music.load('ring_folder/ring.mp3')
		pygame.mixer.music.play()
				
		while pygame.mixer.music.get_busy():
			continue 
			
		
			
	def play(self):
		index = 0
		pygame.mixer.music.set_volume(1.0)
		pygame.mixer.music.load('ring_folder/ring.mp3')
		random.shuffle(self.paths)
		pygame.mixer.music.play()
		while True:
			while pygame.mixer.music.get_busy():
				now = time.localtime()
				current_time = time.strftime("%H:%M")
				if current_time in ['11:25','10:05','13:15','14:15']:
					print('Finishing move')
					self.end()
					while pygame.mixer.music.get_busy():
							continue 
					pygame.mixer.music.stop()
					if current_time == '14:15':
						print("!!! Closing job !!!")
						os.system("shutdown /s /t 0")
					else:
						schedule_task(5,job,special_times)
						return
					
				else:
					continue
			pygame.mixer.music.load('music_folder/'+self.paths[index])
			pygame.mixer.music.play()
			index += 1
			if index == len(paths):
				index = 0
def job():
	job = music_player(paths)
	job.play()		
	
schedule_task(5,job,special_times)
	
		



	


