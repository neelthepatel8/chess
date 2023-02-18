import pygame
from Piece import Piece

class Knight(Piece):
    def __init__(self, image, tile, color):
        super().__init__("Knight", image, tile, color)
    
    def can_move(self, tile):
        tile_pos = tx, ty = tile.row, tile.col
        piece_pos = bx, by = self.tile.row, self.tile.col

        if tile_pos == piece_pos:
            print("Failed same pos")
            return False
        
        if tile.isOutOfBounds(): 
            print("Failed out of bounds")
            return False

        if not (abs(tx - bx) == 2 and abs(ty - by) == 1)\
        and not (abs(tx - bx) == 1 and abs(ty - by) == 2):
            print("Failed Move")
            return False
        
        return True