import pygame
from PIECES import *
from AI import get_random_move, get_ai_move

dark_block = pygame.image.load('assets/customChessSet/board/dark_square.png')
light_block = pygame.image.load('assets/customChessSet/board/light_square.png')
highlight_block = pygame.image.load('assets/customChessSet/board/highlight.png')
dark_block = pygame.transform.scale(dark_block, (75, 75))
light_block = pygame.transform.scale(light_block, (75, 75))
highlight_block = pygame.transform.scale(highlight_block, (75, 75))

whitePawn = pygame.image.load('assets/customChessSet/white/white_pawn.png')
whitePawn = pygame.transform.scale(whitePawn, (75, 75))
whiteRook = pygame.image.load('assets/customChessSet/white/white_rook.png')
whiteRook = pygame.transform.scale(whiteRook, (75, 75))
whiteBishop = pygame.image.load('assets/customChessSet/white/white_bishop.png')
whiteBishop = pygame.transform.scale(whiteBishop, (75, 75))
whiteKnight = pygame.image.load('assets/customChessSet/white/white_knight.png')
whiteKnight = pygame.transform.scale(whiteKnight, (75, 75))
whiteKing = pygame.image.load('assets/customChessSet/white/white_king.png')
whiteKing = pygame.transform.scale(whiteKing, (75, 75))
whiteQueen = pygame.image.load('assets/customChessSet/white/white_queen.png')
whiteQueen = pygame.transform.scale(whiteQueen, (75, 75))

blackPawn = pygame.image.load('assets/customChessSet/black/black_pawn.png')
blackPawn = pygame.transform.scale(blackPawn, (75, 75))
blackRook = pygame.image.load('assets/customChessSet/black/black_rook.png')
blackRook = pygame.transform.scale(blackRook, (75, 75))
blackBishop = pygame.image.load('assets/customChessSet/black/black_bishop.png')
blackBishop = pygame.transform.scale(blackBishop, (75, 75))
blackKnight = pygame.image.load('assets/customChessSet/black/black_knight.png')
blackKnight = pygame.transform.scale(blackKnight, (75, 75))
blackKing = pygame.image.load('assets/customChessSet/black/black_king.png')
blackKing = pygame.transform.scale(blackKing, (75, 75))
blackQueen = pygame.image.load('assets/customChessSet/black/black_queen.png')
blackQueen = pygame.transform.scale(blackQueen, (75, 75))

screen = None
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

def initialize():
    global screen
    pygame.init()
    pygame.display.set_caption('Chess by ABDRH & EESHA')
    icon = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((600, 650))
    screen.fill((0, 0, 0))

def draw_background(board): # this builds the board
    
    block_x = 0
    for i in range(4):
        block_y = 0
        for j in range(4):
            screen.blit(light_block, (block_x, block_y))
            screen.blit(dark_block, (block_x + 75, block_y))
            screen.blit(light_block, (block_x + 75, block_y + 75))
            screen.blit(dark_block, (block_x, block_y + 75))
            block_y += 150
        block_x += 150
    step_x = 0
    step_y = pygame.display.get_surface().get_size()[0] - 75
    for i in range(8):
        for j in range(8):
            if isinstance(board[i][j], ChessPiece):
                obj = globals()[f'{board[i][j].color}{board[i][j].type}']
                screen.blit(obj, (step_x, step_y))
            step_x += 75
        step_x = 0
        step_y -= 75
    pygame.display.update()

def draw_text(text): 
   
    s = pygame.Surface((400, 50), pygame.SRCALPHA)
    s.fill((0, 0, 0, 128))  # Fill it with black color and 50% transparency

    # Position the surface at the center of the screen
    screen_width, screen_height = 600, 650
    s_x = (screen_width - s.get_width()) // 2
    s_y = (screen_height - s.get_height()) // 2
    screen.blit(s, (s_x, s_y))


    text_surface = font.render(text, True, (255, 255, 255))  # White text
    text_x = (screen_width - text_surface.get_width()) // 2
    text_y = s_y + (s.get_height() - text_surface.get_height()) // 2
    screen.blit(text_surface, (text_x, text_y))

    # Render the restart instruction
    text_surface_restart = font.render('PRESS "SPACE" TO RESTART', True, (255, 255, 255))  # White text
    text_x = (screen_width - text_surface_restart.get_width()) // 2
    text_y = s_y + s.get_height() + 10  # 10 pixels below the previous text
    screen.blit(text_surface_restart, (text_x, text_y))

    pygame.display.update()


def get_depth(): # the first screen which gets the depth and shows it also
    
    depth = ""
    font = pygame.font.Font(None, 50)
    input_box = pygame.Rect(200, 300, 250, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False

    # Create a surface for the instruction text
    instruction_font = pygame.font.Font(None, 30)
    instruction_text = instruction_font.render('Enter The Depth You Want :P', True, (12, 54, 64))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            return int(depth)
                        except ValueError:
                            depth = ""
                    elif event.key == pygame.K_BACKSPACE:
                        depth = depth[:-1]
                    else:
                        depth += event.unicode

        screen.fill((30, 30, 30))

        # Load background image
        background_image = pygame.image.load("assets/depthbgimage.png") 
        background_image = pygame.transform.scale(background_image, (600, 650))
        screen.blit(background_image, (0, 0))  # Blit background image at (0,0)


        # Blit the instruction text onto the screen
        screen.blit(instruction_text, (input_box.x-25, input_box.y-40))

        txt_surface = font.render(depth, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

    return depth

def start(board):
    global screen
    possible_piece_moves = []
    running = True
    visible_moves = False
    dimensions = pygame.display.get_surface().get_size()
    game_over = False
    piece = None

   # print(board.game_mode)  # should print 1
   # print(board.ai)  # should print a truthy value


    depth=get_depth()
    draw_background(board) # game starts

    #print(depth)
   # print(board.game_mode)  # should print 1
    #print(board.ai)  # should print a truthy value
    #print(running)
    #draw_background(board)

    if board.game_mode == 1 and board.ai:
        #print(11111)
        get_ai_move(board,depth)
        draw_background(board)


    while running:
        if game_over:
            draw_text(game_over_txt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over: #mouse control 
                x = 7 - pygame.mouse.get_pos()[1] // 75
                y = pygame.mouse.get_pos()[0] // 75
                if isinstance(board[x][y], ChessPiece) and (board.get_player_color() == board[x][y].color or not board.ai) and (x, y) not in possible_piece_moves:
                    piece = board[x][y]
                    moves = piece.filter_moves(piece.get_moves(board), board)
                    move_positions = []
                    possible_piece_moves = []
                    for move in moves:
                        move_positions.append((dimensions[0] - (8 - move[1]) * 75, dimensions[1] - move[0] * 75 - 125))
                        move_x = 7 - move_positions[-1][1] // 75
                        move_y = move_positions[-1][0] // 75
                        possible_piece_moves.append((move_x, move_y))
                    if visible_moves:
                        draw_background(board)
                        visible_moves = False
                    for move in move_positions:
                        visible_moves = True
                        screen.blit(highlight_block, (move[0], move[1]))
                        pygame.display.update()
                else:
                    clicked_move = (x, y)
                    try:
                        if clicked_move in possible_piece_moves:
                            board.make_move(piece, x, y)
                            possible_piece_moves.clear()
                            draw_background(board)
                            if board.ai:
                                get_ai_move(board,depth)
                                draw_background(board)
                                    
                        if board.white_won():
                            game_over = True
                            game_over_txt = 'WHITE WINS!'
                        elif board.black_won():
                            game_over = True
                            game_over_txt = 'BLACK WINS!'
                        elif board.draw():
                            game_over = True
                            game_over_txt = 'DRAW!'
                    except UnboundLocalError:
                        pass
