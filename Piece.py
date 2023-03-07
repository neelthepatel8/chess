import pygame

class Piece:
    def __init__(self, name, image, tile, color):
        self.name = name
        self.image = image
        self.tile = tile
        self.color = color
        self.tile.piece = self
    
    def display(self):
        self.piece = pygame.image.load(self.image).convert_alpha()
        self.piece = pygame.transform.rotozoom(self.piece, 0, 1.5)
        piece_rect = self.piece.get_rect(center = self.tile.surface.center)
        self.rect = piece_rect
        return self.piece, piece_rect
    
    def get_possible_moves(self, board):
        moves = []
        for tile in board:
            if self.can_move(tile):
                moves.append(tile)
            
        return moves
    
    def set_tile(self, tile):
        self.tile = tile