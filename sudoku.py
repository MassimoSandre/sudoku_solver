from xmlrpc.server import DocXMLRPCRequestHandler
from solver import Sudoku_solver
import pygame

class Sudoku:
    def __init__(self, hints=None, solver=None,*, board_pos=(0,0), border=1, cell_size=64) -> None:
        self.__sudoku = hints
        self.__solver = solver

        self.__board_pos = board_pos
        self.__border = border
        self.__cell = cell_size

        self.__highlighted = None


    def update(self):
        self.__solver.update(self.__sudoku)

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.__sudoku[i][j] = 0
        self.__solver.clear()


    def highlight(self, cell):
        if self.__highlighted == cell:
            cell = None
        self.__highlighted = cell
        

    def get_highlighted(self):
        return self.__highlighted

    def set_hints(self, hints):
        self.__sudoku = hints

    def set_solver(self, solver):
        self.__solver = solver

    def get_cell_from_coordinates(self, pos):
        x,y = pos
        bi = (y - self.__board_pos[1]) // (3*self.__cell+self.__border)
        bj = (x - self.__board_pos[0]) // (3*self.__cell+self.__border)

        if bi < 0 or bi >= 3 or bj < 0 or bj >= 3:
            return None

        dx = (x - self.__board_pos[0]) % (3*self.__cell+self.__border)
        dy = (y - self.__board_pos[1]) % (3*self.__cell+self.__border)

        ri = (dy - self.__border) // (self.__cell)
        rj = (dx - self.__border) // (self.__cell)

        if ri < 0 or ri >= 3 or rj < 0 or rj >= 3:
            return None

        fi = bi*3 + ri
        fj = bj*3 + rj
        return (fi,fj)

    def show(self,screen, font):
        sol = self.__solver.get_solution()
        for i in range(9):
            for j in range(9):
                if self.__highlighted == (i,j):
                    color = (60,60,255)
                else:
                    color = (255,255,255)
                pygame.draw.rect(screen, color, pygame.Rect([self.__board_pos[0]+self.__border+j*self.__cell+(j//3*self.__border),self.__board_pos[1]+self.__border+i*self.__cell+(i//3*self.__border)],[self.__cell-1,self.__cell-1]), 0)
                text_surface = None
                if self.__sudoku[i][j] == 0:
                    if sol != None:
                        text_surface = font.render(str(sol[i][j]), False, [220,20,20])
                else:
                    if self.__sudoku != None:
                        text_surface = font.render(str(self.__sudoku[i][j]), False, [0,0,0])

                if text_surface != None:
                    r = text_surface.get_rect()
                    dx,dy = r.width//2, r.height//2
                    x,y = self.__board_pos[0]+self.__border+(j*self.__cell)+self.__cell//2-dx+(j//3*self.__border), self.__board_pos[1]+self.__border+(i*self.__cell)+self.__cell//2-dy+(i//3*self.__border)
                    screen.blit(text_surface, (x,y))
