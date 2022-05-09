from matplotlib.pyplot import text
from solver import Sudoku_solver

sudoku = [
    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,3, 0,8,5],
    # [0,0,1, 0,2,0, 0,0,0],

    # [0,0,0, 5,0,7, 0,0,0],
    # [0,0,4, 0,0,0, 1,0,0],
    # [0,9,0, 0,0,0, 0,0,0],

    # [5,0,0, 0,0,0, 0,7,3],
    # [0,0,2, 0,1,0, 0,0,0],
    # [0,0,0, 0,4,0, 0,0,9]

    
    [0,2,0, 6,0,8, 0,0,0],
    [5,8,0, 0,0,9, 7,0,0],
    [0,0,0, 0,4,0, 0,0,0],

    [3,7,0, 0,0,0, 5,0,0],
    [6,0,0, 0,0,0, 0,0,4],
    [0,0,8, 0,0,0, 0,1,3],

    [0,0,0, 0,2,0, 0,0,0],
    [0,0,9, 8,0,0, 0,3,6],
    [0,0,0, 3,0,6, 0,9,0]


    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,0, 0,0,0],

    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,0, 0,0,0],

    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,0, 0,0,0],
    # [0,0,0, 0,0,0, 0,0,0]
    ]

sol = Sudoku_solver(sudoku)

sol.solve()

for l in sol.get_solution():
    for n in l:
        print(n,end=' ')
    print()

print()
print(sol.is_actually_solved())


import pygame

border = 6
cell = 64
size = width,height= cell*9+4*border,cell*9+4*border

screen = pygame.display.set_mode(size)

pygame.font.init()
f = pygame.font.SysFont('arial', 40)

screen.fill([0]*3)

for i in range(9):
    for j in range(9):
        pygame.draw.rect(screen, [255]*3, pygame.Rect([border+j*cell+(j//3*border),border+i*cell+(i//3*border)],[cell-1,cell-1]), 0)
        if sudoku[i][j] == 0:
            text_surface = f.render(str(sol.get_solution()[i][j]), False, [220,20,20])
            #text_surface = f.render(str(sol.get_solution()[i][j]), False, [255,255,255])
        else:
            text_surface = f.render(str(sol.get_solution()[i][j]), False, [0,0,0])
        r = text_surface.get_rect()
        dx,dy = r.width//2, r.height//2
        print(dx)
        x,y = border+(j*cell)+cell//2-dx+(j//3*border), border+(i*cell)+cell//2-dy+(i//3*border)
        screen.blit(text_surface, (x,y))



pygame.display.update()
pygame.image.save(screen, "solution.png")


