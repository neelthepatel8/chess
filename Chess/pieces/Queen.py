import pygame
from Piece import Piece

class Queen(Piece):
    def __init__(self, image, tile, color):
        super().__init__("Queen", image, tile, color)
    
    def can_move(self, tile):
        tile_pos = tx, ty = tile.row, tile.col
        queen_pos = bx, by = self.tile.row, self.tile.col

        if tile_pos == queen_pos:
            print("Failed same pos")
            return False
        
        if tile.isOutOfBounds(): 
            print("Failed out of bounds")
            return False

        if (tx == bx or ty == by)\
        or abs(tx - bx) == abs(ty - by):
            return True
        
        return False