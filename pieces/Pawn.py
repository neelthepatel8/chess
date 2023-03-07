import pygame
from Piece import Piece
from settings.Color import *

class Pawn(Piece):

    black_start_row = 1
    white_start_row = 6

    def __init__(self, image, tile, color):
        super().__init__("Pawn", image, tile, color)
    
    def can_move(self, tile):
        tile_pos = tx, ty = tile.row, tile.col
        piece_pos = px, py = self.tile.row, self.tile.col

        if tile_pos == piece_pos:
            print("Failed same pos")
            return False
        
        if tile.isOutOfBounds(): 
            print("Failed out of bounds")
            return False

        moving_straight = ty == py

        if not moving_straight:
            return False


        if self.color == Color.black:
            moving_forward = tx > px
            at_start = px == self.black_start_row

        if self.color == Color.white:
            moving_forward = tx < px
            at_start = px == self.white_start_row

        
        if not moving_forward:
            return False
        
        single_move = abs(tx - px) == 1
        double_move = abs(tx - px) == 2

        if double_move and at_start:
            return True
    
        if not single_move:
            return False
        
        return True