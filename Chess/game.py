import pygame
import sys

from Tile import Tile

from piece_imports import *

from Board import Board
from settings.Color import *
from settings.screen_settings import *
from Fen import Fen
from Font import Font

class Chess:

    # ------- INIT ------
    pygame.init()
    font = Font()

    # ------- WINDOW ------
    window = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Chess")

    icon = pygame.image.load('assets/game_icon.png')
    pygame.display.set_icon(icon)

    # ------ BOARD ------
    gameBoard = Board()
    board = gameBoard.tiles
    gameBoard.display_board(window)
    
    # ----- FEN -------
    start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    test_fen = "rnbqk3/ppppbp2/5nrQ/8/8/8/PPPP1PPP/RNB1KBNR"
    fen = Fen(test_fen, board)
    pieces = fen.interpret()
    gameBoard.create_pieces()

    # --------- MAIN LOOP ------
    def run(self):
        moving = False
        gaming = True
        timer = pygame.time.Clock()

        while gaming:

            # --------- EVENT HANDLING -------
            for event in pygame.event.get():
                
                # Quit
                if event.type == pygame.QUIT:
                    gaming = False

                # Piece started moving
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for piece in self.pieces:
                        if piece.rect.collidepoint(event.pos):
                            moving = True
                            currently_moving = piece

                # Piece stopped moving
                elif event.type == pygame.MOUSEBUTTONUP and moving:
                    for row in self.board:
                        for tile in row:
                            if tile.surface.collidepoint(currently_moving.rect.center):
                                if (currently_moving.can_move(tile)):
                                    self.gameBoard.remove_piece(currently_moving.tile)   
                                    currently_moving.rect.center = tile.surface.center
                                    currently_moving.set_tile(tile)
                                    currently_moving.tile.piece = currently_moving 
                                    self.gameBoard.add_piece(currently_moving.tile)   
                                else:
                                    currently_moving.rect.center = currently_moving.tile.surface.center
                                moving = False
                                break

                # Piece is moving
                elif event.type == pygame.MOUSEMOTION and moving:
                    currently_moving.rect.move_ip(event.rel)
                    
            # ------ DISPLAY UPDATE -----
            self.gameBoard.display_board(self.window)
            pygame.display.update()
            timer.tick(FPS)

        else:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    chess = Chess()
    chess.run()