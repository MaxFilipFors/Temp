import pygame as p
from game_engine import Game_state, Move

width = height = 512
dimension = 8
square_size = height // dimension
max_fps = 15 
images = {}


def load_images():
    pieces = ["wP", "wR", "wQ", "wN", "wK", "wB", "bR", "bQ", "bP", "bN", "bK", "bB"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("assets/" + piece + ".png"), (square_size, square_size))




def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = Game_state()
    load_images()
    running = True
    square_selected = () # (row, column)
    player_clicks = [] # [(6,4), (4,4)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                column = location[0]//square_size
                row = location[1]//square_size
                if square_selected == (row, column): #Clicked the same square twice
                    square_selected = ()
                    player_clicks = []
                else:
                    square_selected = (row, column)
                    player_clicks.append(square_selected)
                if len(player_clicks) == 2:
                    move = Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    square_selected = ()
                    player_clicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undo_move()



        draw_game_state(screen, gs)
        clock.tick(max_fps)
        p.display.flip()




def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(dimension):
        for column in range(dimension):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column*square_size, row*square_size, square_size, square_size))



def draw_pieces(screen, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != '  ':
                screen.blit(images[piece], p.Rect(column*square_size, row*square_size, square_size, square_size))



if __name__ == "__main__":
    main()