#-------------------------------------------------------------------------------
# Name:        widgets
# Purpose:	   pygame simple visual controls library
#
# Author:      VoRoN
#
# Created:     20.09.2017
# Copyright:   (c) VoRoN 2017
# Licence:     MIT
#-------------------------------------------------------------------------------
import pygame	

class Screen:
	def __init__(self, config):
		self.name = config['name']
		self.fontCache = FontCache()
		self.background = tuple(config['background'])
		self.controls = []
		for label in (config['labels'] if config.has_key('labels') else []):
			font = self.fontCache.getFont(label['font'], label['font_size'])
			if font == None:
				font = pygame.font.Font(label['font'], label['font_size'])
				self.fontCache.addFont(label['font'], label['font_size'], font)
			h = False
			v = False
			if label.has_key('hvaligment'):
				h = label['hvaligment'][0]
				v = label['hvaligment'][1]
			self.controls.append(Label(font.render(label['text'], True, tuple(label['color'])), tuple(label['position']), h, v))
		
		for picture in (config['pictures'] if config.has_key('pictures') else []):
			image = pygame.image.load(picture['file'])
			self.controls.append(Picture(image, picture['position']))
			
		for button in (config['buttons'] if config.has_key('buttons') else []):
			image = pygame.image.load(button['image'])
			self.controls.append(Button(image, button['position'], button['event']))

	def render(self, screen):
		screen.fill(self.background)
		for control in self.controls:
		    control.render(screen)
  		pygame.draw.rect(screen, (0, 0, 0), [3, 3, 794, 474], 2)
  		
	def onevent(self, event):
		for control in self.controls:
		    if isinstance(control, Button):
		    	control.onevent(event)

class Label:
	def __init__(self, text, position, hcenter = False, vcenter = False):
		self.text = text
		self.position = position
		self.hcenter = hcenter
		self.vcenter = vcenter

	def render(self, screen):
		position = (screen.get_width() / 2 - self.text.get_width() / 2 if self.hcenter else self.position[0],
					screen.get_height() / 2 - self.text.get_height() / 2 if self.vcenter else self.position[1])
		screen.blit(self.text, position)

class Button:
	BTN_STATE_NORM = 0
	BTN_STATE_PUSHED = 1
	EVENT_BUTTONCLICK = pygame.USEREVENT + 2
	
	def __init__(self, image, position, event):
		self.image = image
		self.position = position
		self.event = event
		self.state = Button.BTN_STATE_NORM
		size = image.get_size()
		self.center = (position[0] + size[0] / 2, position[1] + size[1] / 2)
		new_size = tuple(map(lambda(x):int(x * 0.9), size))
		self.image_pushed = pygame.transform.scale(self.image, new_size)
		
	def render(self, screen):
		if self.state == Button.BTN_STATE_NORM:
			screen.blit(self.image, self.position)
		elif self.state == Button.BTN_STATE_PUSHED:
			screen.blit(self.image_pushed, self.position)
		
	def onevent(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and\
		event.button == 1 and\
		self.image.get_rect(center=self.center).collidepoint(event.pos):
			size = self.image.get_size()
			new_size = self.image_pushed.get_size()
			self.position = (self.position[0] + (size[0] - new_size[0]) / 2,
							self.position[1] + (size[1] - new_size[1]) / 2)
			self.state = Button.BTN_STATE_PUSHED
		elif event.type == pygame.MOUSEBUTTONUP and\
		event.button == 1 and self.state == Button.BTN_STATE_PUSHED:
			if self.image.get_rect(center=self.center).collidepoint(event.pos):
				pygame.event.post(pygame.event.Event(Button.EVENT_BUTTONCLICK, {'name':self.event}))
			size = self.image.get_size()
			new_size = self.image_pushed.get_size()
			self.position = (self.position[0] - (size[0] - new_size[0]) / 2,
							self.position[1] - (size[1] - new_size[1]) / 2)
			self.state = Button.BTN_STATE_NORM
			
class Picture:
	def __init__(self, image, position):
		self.image = image
		self.position = position
	def render(self, screen):
		screen.blit(self.image, self.position)

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