import pygame
from settings.Color import *
from Font import *

class Tile:
    def __init__(self, index, pos, row):
        self.index = index
        self.row = row
        self.col = index % 8 if index % 8 != 0 else 8
        self.surface = None
        self.pos = pos
        self.piece = None
        self.color = self.determine_color()  
        self.highlighted = False   

    def determine_color(self):
        if self.row % 2 != 0:
                return Color.black if self.index % 2 == 0 else Color.white
        return Color.white if self.index % 2 == 0 else Color.black

    def isOutOfBounds(self):
        x, y = self.row, self.col
        print(x, y)
        if x > 7 or x < 0: return True
        if y > 7 or y < 0: return True
        return False
    
    def set_highlighted(self):
        self.highlighted = True
    
    def set_text(self, text):
        font = Font()
        color = Color.light_color if self.color == Color.black else Color.dark_color
        text_render = font.open_sans_small.render(text, True, color)
        return text_render