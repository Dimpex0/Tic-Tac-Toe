import pygame as pg
import sys
import pygame.display


class MAIN:
    def __init__(self):
        self.board = [[[pg.Rect(50, 100, 100, 100), "", False], [pg.Rect(150, 100, 100, 100), "", False],
                       [pg.Rect(250, 100, 100, 100), "", False]],
                      [[pg.Rect(50, 200, 100, 100), "", False], [pg.Rect(150, 200, 100, 100), "", False],
                       [pg.Rect(250, 200, 100, 100), "", False]],
                      [[pg.Rect(50, 300, 100, 100), "", False], [pg.Rect(150, 300, 100, 100), "", False],
                       [pg.Rect(250, 300, 100, 100), "", False]]]
        self.horizontal_line_1 = pg.Rect(51, 200, 298, 2)
        self.horizontal_line_2 = pg.Rect(51, 300, 298, 2)
        self.vertical_line_1 = pg.Rect(151, 100, 2, 299)
        self.vertical_line_2 = pg.Rect(251, 100, 2, 299)
        self.player_turns = [['X'], ['O']]
        self.win = False

    def draw_board(self):
        title_font = pg.font.SysFont('timesnewroman', 35)
        text = title_font.render('Tic-Tac-Toe', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = 115
        text_rect.y = 20
        screen.blit(text, text_rect)
        for row in self.board:
            for cell in row:
                pg.draw.rect(screen, (255, 255, 255), cell[0])
        pg.draw.rect(screen, (0, 0, 0), self.horizontal_line_1)
        pg.draw.rect(screen, (0, 0, 0), self.horizontal_line_2)
        pg.draw.rect(screen, (0, 0, 0), self.vertical_line_1)
        pg.draw.rect(screen, (0, 0, 0), self.vertical_line_2)

    def draw_in_cell(self, cell_clicked):
        print(self.player_turns)
        for row in self.board:
            for cell in row:
                if cell[0] == cell_clicked:
                    if cell[1] == '':
                        if self.player_turns[0][0] == 'X':
                            self.draw_x(cell[0].x, cell[0].y)
                            print('yes')
                            cell[1] = 'X'
                            cell[2] = True
                            self.change_turn()
                            break
                        if self.player_turns[0][0] == 'O':
                            self.draw_o(cell[0].x, cell[0].y)
                            print('yes')
                            cell[1] = 'O'
                            cell[2] = True
                            self.change_turn()
                            break

    def check_for_winner(self):
        if self.board[0][0][1] == self.board[0][1][1] == self.board[0][2][1] and self.board[0][0][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[0][0][0].x + 5, self.board[0][0][0].y + 50),
                         (self.board[0][2][0].x + 90, self.board[0][2][0].y + 50), 5)
        if self.board[1][0][1] == self.board[1][1][1] == self.board[1][2][1] and self.board[1][0][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[1][0][0].x + 5, self.board[1][0][0].y + 50),
                         (self.board[1][2][0].x + 90, self.board[1][2][0].y + 50), 5)
        if self.board[2][0][1] == self.board[2][1][1] == self.board[2][2][1] and self.board[2][0][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[2][0][0].x + 5, self.board[2][0][0].y + 50),
                         (self.board[2][2][0].x + 90, self.board[2][2][0].y + 50), 5)
        if self.board[0][0][1] == self.board[1][0][1] == self.board[2][0][1] and self.board[0][0][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[0][0][0].x + 50, self.board[0][0][0].y + 10),
                         (self.board[2][0][0].x + 50, self.board[2][0][0].y + 90), 5)
        if self.board[0][1][1] == self.board[1][1][1] == self.board[2][1][1] and self.board[1][1][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[0][1][0].x + 50, self.board[0][1][0].y + 10),
                         (self.board[2][1][0].x + 50, self.board[2][1][0].y + 90), 5)
        if self.board[0][2][1] == self.board[1][2][1] == self.board[2][2][1] and self.board[0][2][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[0][2][0].x + 50, self.board[0][2][0].y + 10),
                         (self.board[2][2][0].x + 50, self.board[2][2][0].y + 90), 5)
        if self.board[0][0][1] == self.board[1][1][1] == self.board[2][2][1] and self.board[0][0][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[0][0][0].x + 10, self.board[0][0][0].y + 10),
                         (self.board[2][2][0].x + 90, self.board[2][2][0].y + 90), 5)
        if self.board[0][2][1] == self.board[1][1][1] == self.board[2][0][1] and self.board[0][2][1]:
            self.win = True
            pg.draw.line(screen, (0, 0, 0), (self.board[0][2][0].x + 90, self.board[0][2][0].y + 10),
                         (self.board[2][0][0].x + 10, self.board[2][0][0].y + 90), 5)

        if self.win:
            global x_wins, o_wins
            if self.player_turns[0] == ["X"]:
                o_wins += 1
            else:
                x_wins += 1
            title_font = pg.font.SysFont('timesnewroman', 25)
            text = title_font.render('Press R to restart', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.x = 115
            text_rect.y = 420
            screen.blit(text, text_rect)

    def update_score(self):
        rect_x = pg.Rect(25, 50, 90, 40)
        pg.draw.rect(screen, (156, 148, 129), rect_x)

        title_font = pg.font.SysFont('timesnewroman', 35)
        text = title_font.render(f'X - {x_wins}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = 25
        text_rect.y = 50
        screen.blit(text, text_rect)

        rect_o = pg.Rect(280, 52, 130, 40)
        pg.draw.rect(screen, (156, 148, 129), rect_o)
        pg.draw.circle(screen, (0, 0, 0), (300, 70), 15, 2)

        title_font = pg.font.SysFont('timesnewroman', 35)
        text = title_font.render(f' - {o_wins}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = 315
        text_rect.y = 50
        screen.blit(text, text_rect)

    def restart_game(self):
        for row in self.board:
            for cell in row:
                cell[1] = ""
                cell[2] = False
        screen.fill((156, 148, 129))

    def draw_o(self, cell_x, cell_y):
        pg.draw.circle(screen, (0, 0, 0), (cell_x + 50, cell_y + 50), 40, 2)

    def draw_x(self, cell_x, cell_y):
        pg.draw.line(screen, (0, 0, 0), (cell_x + 10, cell_y + 10), (cell_x + 90, cell_y + 90), 2)
        pg.draw.line(screen, (0, 0, 0), (cell_x + 90, cell_y + 10), (cell_x + 10, cell_y + 90), 2)

    def change_turn(self):
        self.player_turns = [self.player_turns[1], self.player_turns[0]]


pg.init()
screen = pg.display.set_mode((400, 500))
pygame.display.set_caption('Tic-Tac-Toe')
clock = pg.time.Clock()

game = MAIN()

x_wins = 0
o_wins = 0

screen.fill((156, 148, 129))
game.draw_board()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                game.restart_game()
                game = MAIN()
                screen.fill((156, 148, 129))
                game.draw_board()
        if event.type == pg.MOUSEBUTTONDOWN and not game.win:
            pos = pg.mouse.get_pos()
            print(pos)
            for row in game.board:
                for cell in row:
                    if cell[0].collidepoint(pos):
                        print(cell[0])
                        game.draw_in_cell(cell[0])
                        game.check_for_winner()

    game.update_score()
    pg.display.update()
    clock.tick(60)
