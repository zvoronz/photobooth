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
from pygame_vkeyboard import *
from os.path import join, dirname

class Screen:
	def __init__(self, config, font_cache, image_cache):
		self.name = config['name']
		self.fontCache = FontCache()
		self.imageCache = image_cache
		self.background = tuple(config['background'])
		self.controls = []
		for label in (config['labels'] if config.has_key('labels') else []):
			h = False
			v = False
			if label.has_key('hvaligment'):
				h = label['hvaligment'][0]
				v = label['hvaligment'][1]
			cntLabel = Label(label['text'], label['color'], label['font'],
							label['font_size'], tuple(label['position']), h, v)
			if label.has_key('zindex'):
				cntLabel.zindex = label['zindex']
			if label.has_key('name'):
				cntLabel.name = label['name']
			self.controls.append(cntLabel)
		
		for picture in (config['pictures'] if config.has_key('pictures') else []):
			image = None
			size = [0, 0]
			name = ''
			if picture.has_key('file'):
				image = self.imageCache.getImage(picture['file'])
			if picture.has_key('size'):
				size = picture['size']
			if picture.has_key('name'):
				name = picture['name']
			cntPiture = Picture(image, picture['position'], size, name)
			if picture.has_key('zindex'):
				cntPiture.zindex = picture['zindex']
			self.controls.append(cntPiture)
			
		for button in (config['buttons'] if config.has_key('buttons') else []):
			image = self.imageCache.getImage(button['image'])
			cntButton = Button(image, button['position'], button['event'])
			if button.has_key('zindex'):
				cntButton.zindex = button['zindex']
			self.controls.append(cntButton)
			
		for textedit in (config['textedits'] if config.has_key('textedits') else []):
			h, v = False, False
			name = ''
			if textedit.has_key('hvaligment'):
				h, v = textedit['hvaligment'][0], textedit['hvaligment'][1]
			if textedit.has_key('name'):
				name = textedit['name']
			textEdit = TextEdit(textedit['position'], textedit['size'],
							 textedit['font'], textedit['font_size'],
							 tuple(textedit['color']), h, v, name)
			textEdit.setText(textedit['text'])
			if textedit.has_key('zindex'):
				textEdit.zindex = textedit['zindex']
			self.controls.insert(0, textEdit)

		self.controls = sorted(self.controls, key=lambda k: k.zindex)
		
	def render(self, screen):
		screen.fill(self.background)
		for control in self.controls:
			try:
				control.render(screen)
			except AttributeError as ex:
				print 'Control do not have \'render\' method'
	
	def onevent(self, event):
		for control in self.controls:
			if isinstance(control, Button):
				event = control.onevent(event)
			if isinstance(control, TextEdit):
				event = control.onevent(event)
			if event == None:
				break

	def getControlByName(self, name):
		for control in self.controls:
			control_name = getattr(control, 'name', '')
			if name == control_name:
				return control
		return None

	def getControlsByType(self, controlType):
		controls = []
		for control in self.controls:
			if isinstance(control, controlType):
				controls.append(control)
		return controls

class Label:
	def __init__(self, text, color, font, font_size, position, hcenter = False,
					vcenter = False, size = None):
		self.text = text
		self.position = position
		self.hcenter = hcenter
		self.vcenter = vcenter
		self.size = size
		self.zindex = 0
		self.font = font
		self.font_size = font_size
		self.fontCache = FontCache()
		self.color = color
		self.fontImg = None
		self.setText(self.text)
		self.name = ''

	def render(self, screen):
		x, y = self.position
		if self.size:
			position = (x + self.size[0] / 2 - self.fontImg.get_width() / 2 if
											self.hcenter else x,
					y + self.size[1] / 2 - self.fontImg.get_height() / 2 if
											self.vcenter else y)
		else:
			position = (screen.get_width() / 2 - self.fontImg.get_width() / 2 if
											self.hcenter else x,
					screen.get_height() / 2 - self.fontImg.get_height() / 2 if
											self.vcenter else y)
		screen.blit(self.fontImg, position)
		
	def setText(self, text):
		self.text = text
		font = self.fontCache.getFont(self.font, self.font_size)
		if font == None:
			font = pygame.font.Font(self.font, self.font_size)
			self.fontCache.addFont(self.font, self.font_size, font)
		self.fontImg = font.render(self.text, True, tuple(self.color))

class MyKeyboardRenderer(VKeyboardRenderer):
	pass
##	def draw_background(self, surface, position, size):
##		pygame.draw.rect(surface, (255, 255, 255, 255),
##			(position[0] + 25, position[1]) + (size[0] - 50, size[1]))

MyKeyboardRenderer.DEFAULT = MyKeyboardRenderer(
	pygame.font.Font('fonts/DejaVuSans.ttf', 25),
	(255, 255, 255),
	((255, 255, 255), (0, 0, 0)),
	((0, 0, 0), (255, 255, 255)),
	((180, 180, 180), (0, 0, 0)),
)

class TextEdit:
	def __init__(self, position, size, font = "fonts/arial.ttf",
							font_size = 20, color = (0, 0, 0),
							hcenter = False, vcenter = False, name = ""):
		self.position = position
		self.size = size
		self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0],
					self.size[1])
		self.keyboard = None
		self.label = None
		self.hcenter = hcenter
		self.vcenter = vcenter
		self.font = font
		self.color = color
		self.font_size = font_size
		self.text = ''
		self.zindex = 0
		self.name = name
		self.label = Label(self.text, color, font, font_size, (position[0] + 2,
							position[1] + 2), hcenter, vcenter, size)
		
	def setText(self, text):
		print text
		self.label.setText(text)
		self.text = text
		
	def getText(self):
		return self.text

	def render(self, screen):
		screen.fill((255, 255, 255), self.rect)
		pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
		if self.keyboard == None:
			self.keyboard = VKeyboard(screen, self.setText,
									VKeyboardLayout(VKeyboardLayout.AZERTY))
##			new_size = (800, 455)
##			self.keyboard.original_layout.configure_bound(new_size)
##			self.keyboard.special_char_layout.configure_bound(new_size)
			self.keyboard.buffer = self.text
			self.keyboardRect = pygame.Rect(self.keyboard.layout.position,
								self.keyboard.layout.size)
		if self.label:
			self.label.render(screen)
			
	def onevent(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				if self.keyboard:
					self.keyboard.enable()
				print 'Text edit click'
			elif self.keyboard and self.keyboard.state > 0\
				and (not self.keyboardRect.collidepoint(event.pos)):
					self.keyboard.disable()
			elif self.keyboard and self.keyboard.state > 0\
				and self.keyboardRect.collidepoint(event.pos):
					event = None
		return event

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
		self.zindex = 0
		
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
				pygame.event.post(pygame.event.Event(Button.EVENT_BUTTONCLICK,
									{'name':self.event}))
			size = self.image.get_size()
			new_size = self.image_pushed.get_size()
			self.position = (self.position[0] - (size[0] - new_size[0]) / 2,
							self.position[1] - (size[1] - new_size[1]) / 2)
			self.state = Button.BTN_STATE_NORM
		return event
			
class Picture:
	def __init__(self, image, position, size, name):
		self.image = image
		self.position = position
		self.size = size
		self.name = name
		self.zindex = 0
		
	def render(self, screen):
		if self.image != None:
			screen.blit(self.image, self.position)

def singleton(cls):
	instances = {}
	def getinstance():
		if cls not in instances:
			instances[cls] = cls()
		return instances[cls]
	return getinstance

@singleton
class ImageCache:
	def __init__(self):
		self.images = []
		
	def getImage(self, image_path):
		for image in self.images:
			if image['path'] == image_path:
				return image['image']
		image = pygame.image.load(image_path)
		self.images.append({'path':image_path, 'image':image})
		return image

@singleton
class FontCache:
	def __init__(self):
		self.fonts = []

	def getFont(self, name, size):
		for font in self.fonts:
			if font['name'] == name and font['size'] == size:
				return font['font']
		return None

	def addFont(self, name, size, font):
		self.fonts.append({'name':name, 'size':size, 'font':font})