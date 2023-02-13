import pygame
from Piece import Piece
from Tile import Tile

class Bishop(Piece):
    def __init__(self, image, tile):
        super().__init__("Bishop", image, tile)
    
    def can_move(self, tile):
        tile_pos = tx, ty = tile.row, tile.col
        bishop_pos = bx, by = self.tile.row, self.tile.col

        if tile_pos == bishop_pos:
            print("Failed same pos")
            return False
        
        if tile.isOutOfBounds(): 
            print("Failed out of bounds")
            return False

        if abs(tx - bx) != abs(ty - by):
            print("Failed diagnol")
            return False
        
        return True
    
    def get_possible_moves(self, board):
        moves = []
        for tile in board:
            if not tile: continue
            if self.can_move(tile):
                moves.append(tile)
            
        return moves

