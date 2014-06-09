__author__ = 'iwcrosby'

import pygame

class button:
    '''A clickable button. Coordinate tuple p is the location. w and h are the width and height.'''

    def __init__(self, w=1, h=1, p=(0,0), label="no label"):

        self.rect = pygame.Rect(p,(w,h))
        self.label = label
