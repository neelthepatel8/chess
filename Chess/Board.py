from colors import *
from screen_settings import *
from Tile import Tile

class Board:

    TILE_SIZE = SCREEN_SIZE_X / 8

    def __init__(self):
        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        x, y = 0, 0
        row = 1
        self.tiles.append(None)
        for i in range(1, 65):
            self.tiles.append(Tile(i, (x, y), row))

            if i % 8 == 0:
                x = 0
                y += self.TILE_SIZE
                row += 1
            else : x += self.TILE_SIZE

    def display_board(self, window):
        for tile in self.tiles:
            if tile == None: continue
            color = DARK_COLOR if tile.color == 'BLACK' else LIGHT_COLOR
            tile_surface = pygame.draw.rect(window, color, pygame.Rect(tile.pos, (self.TILE_SIZE, self.TILE_SIZE)))
            tile.surface = tile_surface
            window.blit(tile.piece)
    