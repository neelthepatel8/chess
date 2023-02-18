from settings.Color import *
from settings.screen_settings import *
from Tile import Tile

class Board:

    TILE_SIZE = SCREEN_SIZE_X / 8

    def __init__(self):
        self.tiles = []
        self.create_tiles()
        self.pieces = {}

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

    def create_pieces(self):

        for row in self.tiles:
            for tile in row:
                if tile.piece:
                    self.pieces[tile] = {}
                    p, prect = tile.piece.display()
                    self.pieces[tile]["piece"] = p
                    self.pieces[tile]["piece_rect"] = prect

    def display_board(self, window):
        for row in self.tiles:
            for tile in row:
                color = Color.dark_color if tile.color == Color.black else Color.light_color
                if tile.highlighted:
                    color = Color.highlight_color
                tile_surface = pygame.draw.rect(window, color, pygame.Rect(tile.pos, (self.TILE_SIZE, self.TILE_SIZE)))
                tile.surface = tile_surface

        for piece in self.pieces:
            window.blit(self.pieces[piece]["piece"], self.pieces[piece]["piece_rect"])
    
    def remove_piece(self, tile):
        self.pieces.pop(tile)
    
    def add_piece(self, tile):
        self.pieces[tile] = {}
        p, prect = tile.piece.display()
        self.pieces[tile]["piece"] = p
        self.pieces[tile]["piece_rect"] = prect