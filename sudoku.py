""" 
Sodoku module

The Sudoku class allows the user to draw and handle a sudoku puzzle

    Usage example:

    game = Sudoku(hints, solver,board_pos, border, cell_size)
"""

from sudoku_solver import Sudoku_solver
import pygame

class Sudoku:
    """
    A class designed to draw and handle a sudoku puzzle

    Attributes:
        __sudoku: A 9x9 matrix representing a sudoku puzzle
        __solver: A Sudoku_solver object handled by the class itself
        __board_pos: A tuple of 2 integers, representing the position (in pixel) of the top-left corner of the board
        __border: An integer, representing the width of the board's border. It's also the border between 3x3 areas of the sudoku puzzle
        __cell: An integer, representing the size of the cell of the sudoku
        __highlighted: A tuple of 2 integers, containing the indexes of the selected/highlighted cell of the sudoku puzzle
    """

    def __init__(self, hints:list[list[int]]=None, solver:Sudoku_solver=None,*, board_pos=(0,0), border:int=1, cell_size:int=64) -> None:
        """
        Inits Sudoku

        Args:
            hints: A 9x9 matrix representing a sudoku puzzle
            solver: A Sudoku_solver object
            board_pos: A tuple of 2 integers, representing the position (in pixel) of the top-left corner of the board
            border: An integer, representing the width of the board's border. It's also the border between 3x3 areas of the sudoku puzzle
            cell_size: An integer, representing the size of the cell of the sudoku
        """
        self.__sudoku = hints
        self.__solver = solver

        self.__board_pos = board_pos
        self.__border = border
        self.__cell = cell_size

        self.__highlighted = None


    def update(self) -> None:
        """
        Updates the solver

        Makes sure that the current puzzle stored in the Sudoku class is
        compatible with the one stored in the solver
        """
        self.__solver.update(self.__sudoku)

    def clear(self) -> None:
        """
        Clears the current sudoku

        When used the sudoku is lost
        It also clears the solver
        """
        for i in range(9):
            for j in range(9):
                self.__sudoku[i][j] = 0
        self.__solver.clear()


    def highlight(self, cell) -> None:
        """
        Highlight the specified cell in the sudoku

        It works as a toggler if the cell is already highlighted

        Args:
            cell: A tuple of 2 integers, containing the indexes of the selected/highlighted cell of the sudoku puzzle
        """
        if self.__highlighted == cell:
            cell = None
        self.__highlighted = cell
        

    def get_highlighted(self):
        """
        Returns:
            the indexes of the currently highlighted cell, None if there is no highlighted cell
        """
        return self.__highlighted

    def set_hints(self, hints:list[list[int]]) -> None:
        """
        Sets a new sudoku

        When used the previous sudoku is lost.
        The solver's sudoku is also updated

        Args:
            hints: A 9x9 matrix representing a sudoku puzzle
        """
        self.__sudoku = hints
        self.solver.set_sudoku(hints)

    def set_solver(self, solver:Sudoku_solver) -> None:
        """
        Sets a new solver

        Args:
            solver: A Sudoku_solver object which willl be handled by the class itself from now on 
        """
        self.__solver = solver

    def get_cell_from_coordinates(self, pos):
        """
        Calculates the indexes of the cell in which an absolute position lays

        Args:
            pos: A tuple of 2 integers representing an absolute position (in pixel)
        
        Returns:
            The indexes of the cell in which the provided position lays
        """
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

    def show(self,screen:pygame.Surface, font:pygame.font.Font) -> None:
        """
        Shows the sudoku puzzle

        Args:
            screen: The pygame surface where the sudoku puzzle will be drawn
            font: the pygame font for the digits
        """
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
