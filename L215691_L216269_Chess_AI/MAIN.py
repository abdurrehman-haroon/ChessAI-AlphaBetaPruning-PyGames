import GUI
from BOARD import *


if __name__ == '__main__':
    keep_playing = True

    board = Board(game_mode=0, ai=True) 

    while keep_playing:
        GUI.initialize()
        board.place_pieces()
        GUI.draw_background(board)
        keep_playing = GUI.start(board)
        