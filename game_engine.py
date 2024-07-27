import numpy as np


class Game_state():
    def __init__(self):
        self.board = np.array([
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ])
        self.white_to_move = True
        self.moveLog = []

    def make_move(self, move):
        self.board[move.start_row][move.start_column] = '  '
        self.board[move.end_row][move.end_column] = move.pieceMoved
        self.moveLog.append(move)
        self.white_to_move = not self.white_to_move


    def undo_move(self):
        if len(self.moveLog) != 0:
            move_to_undo = self.moveLog.pop()
            self.board[move_to_undo.end_row][move_to_undo.end_column] = '  '
            self.board[move_to_undo.start_row][move_to_undo.start_column] = move_to_undo.pieceMoved
            self.white_to_move = not self.white_to_move

class Move():
    def __init__(self, start, end, board):
        self.start_row = start[0]
        self.start_column = start[1]
        self.end_row = end[0]
        self.end_column = end[1]
        self.pieceMoved = board[self.start_row][self.start_column]
        self.pieceCaptured = board[self.end_row][self.end_column]

    def get_chess_notation(self):
        return self._to_chess_notation(self.start_row, self.start_column) + self._to_chess_notation(self.end_row, self.end_column)

    def _to_chess_notation(self, row, column):
        return chr(column + ord('a')) + str(8 - row)

    @staticmethod
    def from_chess_notation(chess_notation):
        column = ord(chess_notation[0]) - ord('a')
        row = 8 - int(chess_notation[1])
        return row, column
     