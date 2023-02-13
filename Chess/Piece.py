import pygame

class Piece:
    def __init__(self, name, image, tile):
        self.name = name
        self.image = image
        self.tile = tile
        self.tile.piece = self
        self.rect = None
        self.focus = False
    
    def display(self):
        piece = pygame.image.load(self.image).convert_alpha()
        piece = pygame.transform.rotozoom(piece, 0, 1.5)
        piece_rect = piece.get_rect(center = self.tile.surface.center)
        self.rect = piece_rect
        return piece, piece_rect
    
    def set_tile(self, tile):
        self.tile = tile
    
    
    def is_clicked(self):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True