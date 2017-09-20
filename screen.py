#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VoRoN
#
# Created:     20.09.2017
# Copyright:   (c) VoRoN 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame

class Screen:
	def __init__(self, config):
		self.fontCache = FontCache()
		self.background = tuple(config['background'])
		self.labels = []
		for label in config['labels']:
			font = self.fontCache.getFont(label['font'], label['font_size'])
			if font == None:
				font = pygame.font.SysFont(label['font'], label['font_size'], True)
				self.fontCache.addFont(label['font'], label['font_size'], font)
			self.labels.append(Label(font.render(label['text'], True, tuple(label['color'])),
									tuple(label['position'])))
	def render(self, screen):
		screen.fill(self.background)
		for label in self.labels:
		    label.render(screen)

class Label:
	def __init__(self, text, position):
		self.text = text
		self.position = position
	def render(self, screen):
		position = (screen.get_width() / 2 - self.text.get_width() / 2,
					screen.get_height() / 2 - self.text.get_height() / 2)
		screen.blit(self.text, position)

class FontCache:
	def __init__(self):
		self.fonts = []

	def getFont(self, name, size):
		for font in self.fonts:
			if font['name'] == name and font['size'] == size:
				return font['font']
			else:
				return None

	def addFont(self, name, size, font):
		self.fonts.append({'name':name, 'size':size, 'font':font})