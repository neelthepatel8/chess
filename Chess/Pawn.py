import pygame
from Piece import Piece
from Color import *

class Pawn(Piece):

    black_start_row = 6
    white_start_row = 1

    def __init__(self, image, tile, color):
        super().__init__("Pawn", image, tile, color)
    
    def can_move(self, tile):
        tile_pos = tx, ty = tile.row, tile.col
        piece_pos = bx, by = self.tile.row, self.tile.col

        if tile_pos == piece_pos:
            print("Failed same pos")
            return False
        
        if tile.isOutOfBounds(): 
            print("Failed out of bounds")
            return False

        if ty != by:
            return False

        if self.color == Color.black and (abs(tx - bx) > 2 or tx - bx > 0):
            return False
        if self.color == Color.white and (abs(tx - bx) > 2 or tx - bx < 0)):
            return False

        if abs(tx - bx) == 2:
            if self.color == Color.black:
                return bx == self.black_start_row
        if self.color == Color.white:
            return bx == self.white_start_row;
        
        return True