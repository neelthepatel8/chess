import pygame
import sys

from Tile import Tile

from piece_imports import *

from Board import Board
from settings.Color import *
from settings.screen_settings import *
from Fen import Fen

# ------- INIT ------
pygame.init()

# ------- WINDOW ------
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Chess")

icon = pygame.image.load('assets/game_icon.png')
pygame.display.set_icon(icon)


# ------ BOARD ------
gameBoard = Board()
board = gameBoard.tiles
gameBoard.display_board(window)

# Generate black pieces
start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

test_fen = "r2qkb1r/ppp2Qpp/2np4/6Pn/2BpP1b1/8/PPP2P1P/RNB1K1NR"
fen = Fen(test_fen, board)
pieces = fen.interpret()

gameBoard.create_pieces()

moving = False

# --------- MAIN LOOP ------
while True:

    # --------- EVENT HANDLING -------
    for event in pygame.event.get():
        
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Piece started moving
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for piece in pieces:
                if piece.rect.collidepoint(event.pos):
                    moving = True
                    currently_moving = piece

        # Piece stopped moving
        elif event.type == pygame.MOUSEBUTTONUP and moving:
            for row in board:
                for tile in row:
                    if tile.surface.collidepoint(currently_moving.rect.center):
                        if (currently_moving.can_move(tile)):
                            gameBoard.remove_piece(currently_moving.tile)   
                            currently_moving.rect.center = tile.surface.center
                            currently_moving.set_tile(tile)
                            currently_moving.tile.piece = currently_moving 
                            gameBoard.add_piece(currently_moving.tile)   
                        else:
                            currently_moving.rect.center = currently_moving.tile.surface.center
                        moving = False
                        break

        # Piece is moving
        elif event.type == pygame.MOUSEMOTION and moving:
            currently_moving.rect.move_ip(event.rel)
            

    gameBoard.display_board(window)

    # ----- GAME PLAY -----
    pygame.display.update()