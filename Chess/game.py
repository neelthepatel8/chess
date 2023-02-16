import pygame
import sys

from Tile import Tile
from Piece import Piece
from Bishop import Bishop
from Knight import Knight
from Board import Board
from Color import *
from screen_settings import *

# ------- INIT ------
pygame.init()

# ------- WINDOW ------
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Chess")


# ------ BOARD ------
gameBoard = Board()
board = gameBoard.tiles
gameBoard.display_board(window)

# Generate black pieces
bishop = Bishop('assets/pieces/bishop_black.png', board[7][2])
knight = Knight('assets/pieces/knight_black.png', board[7][1])

pieces = [bishop, knight]

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
                            currently_moving.rect.center = tile.surface.center
                            currently_moving.tile.piece = None
                            currently_moving.set_tile(tile)
                            currently_moving.tile.piece = currently_moving
                        else:
                            currently_moving.rect.center = currently_moving.tile.surface.center
                        moving = False
                        break

        # Piece is moving
        elif event.type == pygame.MOUSEMOTION and moving:
            currently_moving.rect.move_ip(event.rel)
            print(f"moved {currently_moving} to {currently_moving.rect.center}")
            if not currently_moving.rect.collidepoint(pygame.mouse.get_pos()):
                currently_moving.rect.center = pygame.mouse.get_pos()
            

    gameBoard.display_board(window)

    # ----- GAME PLAY -----
    pygame.display.update()