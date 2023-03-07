import pygame


class Font:

    def __init__(self):
        self.open_sans_small = pygame.font.Font("assets/fonts/open_sans/static/OpenSans/OpenSans-Bold.ttf", 18)        
        self.open_sans_medium = pygame.font.Font("assets/fonts/open_sans/static/OpenSans/OpenSans-Bold.ttf", 32)        
        self.open_sans_large = pygame.font.Font("assets/fonts/open_sans/static/OpenSans/OpenSans-Bold.ttf", 48)        