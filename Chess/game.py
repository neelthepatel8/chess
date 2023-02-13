import pygame
import sys

from Tile import Tile
from Piece import Piece
from Bishop import Bishop
from Board import Board
from colors import *
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
bishop = Bishop('assets/pieces/bishop_black.png', board[13])
b, brect = bishop.display()
window.blit(b, brect)

moving = False

current_highlighted = []
# --------- MAIN LOOP ------
while True:

    gameBoard.display_board(window)

    # --------- EVENT HANDLING -------
    for event in pygame.event.get():
        
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        # Piece started moving
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if brect.collidepoint(event.pos):
                moving = True

        # Piece stopped moving
        elif event.type == pygame.MOUSEBUTTONUP:
            if brect.collidepoint(event.pos):
                for tile in board:
                    if tile == None: continue
                    if tile.surface.collidepoint(brect.center):
                        if (bishop.can_move(tile)):
                            brect.center = tile.surface.center;
                            bishop.set_tile(tile)
                        else:
                            brect.center = bishop.tile.surface.center
                        moving = False
                        break

        # Piece is moving
        elif event.type == pygame.MOUSEMOTION and moving:
            brect.move_ip(event.rel)
            if not brect.collidepoint(pygame.mouse.get_pos()):
                brect.center = pygame.mouse.get_pos()
            
    # ----- GAME PLAY -----
    pygame.display.update()