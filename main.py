import pygame
from solver import Sudoku_solver
from button import Button
from sudoku import Sudoku

hints = [   
    # [0,2,0, 6,0,8, 0,0,0],
    # [5,8,0, 0,0,9, 7,0,0],
    # [0,0,0, 0,4,0, 0,0,0],

    # [3,7,0, 0,0,0, 5,0,0],
    # [6,0,0, 0,0,0, 0,0,4],
    # [0,0,8, 0,0,0, 0,1,3],

    # [0,0,0, 0,2,0, 0,0,0],
    # [0,0,9, 8,0,0, 0,3,6],
    # [0,0,0, 3,0,6, 0,9,0]


    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],

    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],

    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0]
    ]


board_pos = 0,0
border = 4
cell_size = 64

button_size = 200,80
button_margin = 40

size = width,height= cell_size*9+4*border,cell_size*9+4*border + 2*button_margin + button_size[1]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sudoku solver')

pygame.font.init()

f = pygame.font.SysFont('arial', 40)
button_font = pygame.font.SysFont('arial', 30)

clock = pygame.time.Clock()

solver = Sudoku_solver(hints)
sudoku = Sudoku(hints,solver,board_pos=board_pos,border=border,cell_size=cell_size)

buttons = []
buttons.append(Button(pos=(width//4,height-(button_margin+button_size[1]//2)), width=button_size[0], height=button_size[1], value="Solve", font=button_font, onclick=solver.solve))
buttons.append(Button(pos=(width//4*3,height-(button_margin+button_size[1]//2)), width=button_size[0], height=button_size[1], value="Clear", font=button_font, onclick=sudoku.clear))

running = True

hints_edited = False
while running:
    screen.fill([0]*3)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                sudoku.highlight(sudoku.get_cell_from_coordinates(event.pos))

                for b in buttons:
                    if b.is_inside(event.pos):
                        b.click()
            elif event.button == 3:
                sudoku.highlight(None)
                c = sudoku.get_cell_from_coordinates(event.pos)
                if c != None:
                    i,j = c
                    if hints[i][j] != 0:
                        hints_edited=True
                        hints[i][j] = 0
                    
        elif event.type == pygame.KEYDOWN:
            try: 
                i,j = sudoku.get_highlighted()
            except:
                continue

            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                sudoku.highlight(None)
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_0:
                if hints[i][j] != 0:
                    hints_edited=True
                hints[i][j] = 0
            elif event.key == pygame.K_1:
                if hints[i][j] != 1:
                    hints_edited=True
                hints[i][j] = 1
            elif event.key == pygame.K_2:
                if hints[i][j] != 2:
                    hints_edited=True
                hints[i][j] = 2
            elif event.key == pygame.K_3:
                if hints[i][j] != 3:
                    hints_edited=True
                hints[i][j] = 3
            elif event.key == pygame.K_4:
                if hints[i][j] != 4:
                    hints_edited=True
                hints[i][j] = 4
            elif event.key == pygame.K_5:
                if hints[i][j] != 5:
                    hints_edited=True
                hints[i][j] = 5
            elif event.key == pygame.K_6:
                if hints[i][j] != 6:
                    hints_edited=True
                hints[i][j] = 6
            elif event.key == pygame.K_7:
                if hints[i][j] != 7:
                    hints_edited=True
                hints[i][j] = 7
            elif event.key == pygame.K_8:
                if hints[i][j] != 8:
                    hints_edited=True
                hints[i][j] = 8
            elif event.key == pygame.K_9:
                if hints[i][j] != 9:
                    hints_edited=True
                hints[i][j] = 9

    buttons[0].disabled = solver.is_actually_solved()

    if hints_edited:
        sudoku.update()
        hints_edited = False

    sudoku.show(screen,f)
    for b in buttons:
        b.show(screen,pygame.mouse.get_pos())
      

    pygame.display.update()
    clock.tick(60)



