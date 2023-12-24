import sys
import pygame


def include_images():
	"""Функция добавления изображений в список"""
	images = []
	# в цикле задаётся количество добавляемых картинок
	for i in range(0, 6):
		images.append(pygame.image.load(f'images/{i}.bmp'))
	return images
	

def check_events(current_image):
	"""Функция обработки событий"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# обработка нажатия клавиш
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				# уменьшение индекса при нажатии K_LEFT
				current_image -= 1
				break
			elif event.key == pygame.K_RIGHT:
				# увеличение индекса при нажатии K_RIGHT
				current_image += 1
				break
			# закрытие окна при нажатии ESC
			elif event.key == pygame.K_ESCAPE:
				sys.exit()
	# возврат изменённого индекса			
	return current_image


def color_from_screen(images, current_image):
	"""Функция обесцвечивания выбранного цвета на картинке"""
	# данные цвета пикселя на фоне картинки по координатам
	pixel_color = images[current_image].get_at((5, 5))
	# применение обесцвечивания для выбранного цвета фона
	images[current_image].set_colorkey(pixel_color)
	# преобразование картинки с прозрачностью
	images[current_image] = images[current_image].convert_alpha()
	

def color_from_image(images, current_image):
	"""Функция передачии данных о цвете фона изображения"""
	# данные цвета пикселя на фоне картинки по координатам
	pixel_color = images[current_image].get_at((5, 5))
	# преобразование картинки
	images[current_image] = images[current_image].convert()
	# возврат цвета пикселя
	return pixel_color 
	

def image_location(images, current_image, screen):
	"""Функция отрисовки изображения на экране"""
	# получение прямоугольной отрисовки экрана
	screen_rect = screen.get_rect()
	# получение прямоугольной отрисовки изображения
	rect = images[current_image].get_rect()

	# задание мета отрисовки изображения по центру экрана	
	rect.centerx = screen_rect.centerx
	rect.centery = screen_rect.centery
	
	# отрисовка изображения на экране
	screen.blit(images[current_image], rect)
