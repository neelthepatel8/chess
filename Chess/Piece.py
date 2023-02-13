import pygame

class Piece:
    def __init__(self, name, image, tile):
        self.name = name
        self.image = image
        self.tile = tile
    
    def display(self):
        piece = pygame.image.load(self.image).convert_alpha()
        piece = pygame.transform.rotozoom(piece, 0, 1.5)
        piece_rect = piece.get_rect(center = self.tile.surface.center)
        self.rect = piece_rect
        return piece, piece_rect
    
    def get_possible_moves(self, board):
        moves = []
        for tile in board:
            if not tile: continue
            if self.can_move(tile):
                moves.append(tile)
            
        return moves