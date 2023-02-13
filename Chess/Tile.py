import pygame

class Tile:
    def __init__(self, index, pos, row):
        self.index = index
        self.row = row
        self.col = index % 8 if index % 8 != 0 else 8
        self.surface = None
        self.pos = pos
        self.piece = None
        self.coords = self.determine_coords()
        self.color = self.determine_color()     

    def determine_coords(self):
        rows = [None, '8', '7', '6', '5', '4', '3', '2', '1']
        cols = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        return cols[self.index % 8] + rows[self.row] if self.index % 8 != 0 else 'h' + rows[self.row]

    def determine_color(self):
        if self.row % 2 != 0:
                return 'BLACK' if self.index % 2 == 0 else 'WHITE'
        return 'WHITE' if self.index % 2 == 0 else 'BLACK'

    def isOutOfBounds(self):
        x, y = self.row, self.col

        if x > 8 or x < 1: return True
        if y > 8 or y < 1: return True
        return False