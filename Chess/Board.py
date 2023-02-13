from colors import *
from screen_settings import *
from Tile import Tile
from pprint import pprint

class Board:

    TILE_SIZE = SCREEN_SIZE_X / 8

    def __init__(self):
        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        x, y = 0, 0
        index = 0
        for row in range(8):
            self.tiles.append([])
            for col in range(8):
                tile = Tile(index, (x, y), row)
                self.tiles[row].append(tile)
                index += 1  
                x += self.TILE_SIZE
            x = 0
            y += self.TILE_SIZE

    def display_board(self, window):
        for row in self.tiles:
            for tile in row:
                color = DARK_COLOR if tile.color == 'BLACK' else LIGHT_COLOR
                tile_surface = pygame.draw.rect(window, color, pygame.Rect(tile.pos, (self.TILE_SIZE, self.TILE_SIZE)))
                tile.surface = tile_surface
                window.blit(tile.piece.display())
        