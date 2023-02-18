from settings.Color import Color
from piece_imports import *
from pprint import pprint

class Fen:

    fen_key = {
        "r" : Rook,
        "n" : Knight,
        "b" : Bishop,
        "q" : Queen,
        "k" : King,
        "p" : Pawn
    }
    image_key = {
        "r" : "assets/pieces/rook",
        "n" : "assets/pieces/knight",
        "b" : "assets/pieces/bishop",
        "q" : "assets/pieces/queen",
        "k" : "assets/pieces/king",
        "p" : "assets/pieces/pawn"
    }


    def __init__(self, fen, board):
        self.string = fen
        self.board = board
    
    def interpret(self):
        pieces = []
        for row_num, row in enumerate(self.string.split("/")):
            pieces += self.interpret_row(row, row_num)
            print(row)
            print(row_num)
        
        return pieces
            
    def interpret_row(self, row, row_num):

        pieces = []

        for col, letter in enumerate(row):
            if letter.isnumeric():
                continue
                
            if letter.isupper():
                color = Color.white
            else: color = Color.black
        
            piece = self.fen_key[letter.lower()]
            pieces.append (piece(
                f"{self.image_key[letter.lower()]}_{color}.png", 
                self.board[row_num][col],
                color));
        
        return pieces
