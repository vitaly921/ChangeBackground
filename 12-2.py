# 12-2. Задание цвета фона картинки в соответствии с цветом фона экрана
import pygame
import sys 
import game_functions as gf


def run_game():
	pygame.init()
	# настройка экрана (разрешение, название, цвет фона)
	screen = pygame.display.set_mode((1200, 600))
	background_screen = (10, 136, 225)
	pygame.display.set_caption('Changing the background image/screen')
	
	# добавление изображений в список
	images = gf.include_images()
	
	# задание начального индекса в списке изображений
	current_image = 0
	
	# основной цикл
	while True:
		# обновление индекса после обработки событий
		current_image = gf.check_events(current_image)		
		try:
			# 1 ВАРИАНТ. изменение фона картинки на фон экрана
			#gf.color_from_screen(images, current_image)
			
			# 2 ВАРИАНТ. изменение фона экрана на фон картинки	
			pixel_color = gf.color_from_image(images, current_image)
		# обработка ошибки выхода за пределы массива изображений	
		except IndexError:
			current_image = 0
		
		# 1 ВАРИАНТ. изменение фона картинки на фон экрана
		#screen.fill(background_screen)
		# 2 ВАРИАНТ. изменение фона экрана на фон картинки	
		screen.fill(pixel_color)
		
		# отрисовка картинки на экране
		gf.image_location(images, current_image, screen)
		
		# обновление экрана
		pygame.display.flip()

# запуск программы
run_game()
