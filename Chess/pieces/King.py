import pygame
from Piece import Piece

class King(Piece):
    def __init__(self, image, tile, color):
        super().__init__("King", image, tile, color)
    
    def can_move(self, tile):
        tile_pos = tx, ty = tile.row, tile.col
        piece_pos = bx, by = self.tile.row, self.tile.col

        if tile_pos == piece_pos:
            print("Failed same pos")
            return False
        
        if tile.isOutOfBounds(): 
            print("Failed out of bounds")
            return False

        if abs(tx - bx) <= 1 and abs(ty - by) <= 1:
            return True
        return False