""" 
Sodoku solver module

The Sudoku_solver class implements an algorithm designed to solve
standard 9x9 Sudokus.

    Usage example:

    solver = Sudoku_solver()
    solver.set_sudoku(puzzle)
    solver.solve()
    solution = solver.get_solution()
"""

class Sudoku_solver:
    """
    A class designed to solve standard sudoku

    Attributes:
        __sudoku: A 9x9 matrix representing a sudoku puzzle
    """
    
    def __init__(self, sudoku:list[list[int]]=None) -> None:
        """
        Inits Sudoku_solver

        The user might want to provide the sudoku now, but it's not mandatory

        Args:
            sudoku: A 9x9 matrix representing a sudoku puzzle
        """
        if sudoku == None:
            self.__sudoku = None
        else:
            self.__sudoku = [[sudoku[i][j] for j in range(9)] for i in range(9)]
        
    def set_sudoku(self, sudoku:list[list[int]]) -> None:
        """
        Sets a new sudoku

        When used the previous sudoku is lost and the solver is ready to solve the new one

        Args:
            sudoku: A 9x9 matrix representing a sudoku puzzle
        """
        self.__sudoku = [[sudoku[i][j] for j in range(9)] for i in range(9)]
        

    def clear(self) -> None:
        """
        Clears the current sudoku

        When used the sudoku is lost
        """
        self.__sudoku = [[0 for j in range(9)] for i in range(9)]

    def update(self, sudoku:list[list[int]]) -> None:
        """
        Updates the current sudoku to make it compatible with another one

        If the two sudokus aren't compatible, update acts exactly like set_sudoku
        
        Args:
            sudoku: A 9x9 matrix representing a sudoku puzzle
        """
        if not self.is_actually_solved():
            self.set_sudoku(sudoku)
        for i in range(9):
            for j in range(9):
                if self.__sudoku[i][j] != sudoku[i][j] and sudoku[i][j] != 0:
                    self.set_sudoku(sudoku)
                    return
        


    def get_solution(self) -> list[list[int]]:
        """
        Returns the solution of the solved sudoku puzzle

        If the submitted sudoku puzzle is actually solvable, the 
        method returns the solutions, otherwise it will return None
        
        Returns:
            A 9x9 matrix representing the solution of a sudoku puzzle
            if the submitted sudoku puzzle is unsolvable, the method will
            return None
        """
        if self.is_actually_solved():
            return [[self.__sudoku[i][j] for j in range(9)] for i in range(9)]
        else:
            return None

    def print_sudoku(self) -> None:
        """
        (DEBUG) Prints the currently stored sudoku

        Prints the data currently stored in the __sudoku attribute,
        regardless of whether it is solved or not
        """
        for l in self.__sudoku:
            for n in l:
                print(n,end=' ')
            print()

        print()


    def is_actually_solved(self) -> bool:
        """
        Checks if the sudoku puzzle is solved

        Checks if the data currently stored in the __sudoku attribute represents a valid
        sudoku solution

        Returns:
            True if the sudoku puzzle is solved, False if not
        """
        if self.__sudoku == None:
            return False
        for i in range(9):
            for j in range(9):
                nums1 = [x for x in range(1,10)]
                nums2 = [x for x in range(1,10)]
                nums3 = [x for x in range(1,10)]
                for k in range(9):
                    if self.__sudoku[i][k] in nums1:
                        nums1.remove(self.__sudoku[i][k])
                    if self.__sudoku[k][j] in nums2:
                        nums2.remove(self.__sudoku[k][j])

                sqi = (i//3)*3
                sqj = (j//3)*3
                for k in range(3):
                    for h in range(3):
                        if self.__sudoku[sqi+k][sqj+h] in nums3:
                            nums3.remove(self.__sudoku[sqi+k][sqj+h])

                if len(nums1) + len(nums2) + len(nums3) != 0:
                    return False
        
        return True

    def solve(self) -> None:
        """
        Solve the sudoku

        If possible, finds a solution for the sudoku puzzle currently stored in the __sudoku attribute
        The algorithm might need a few seconds to solve difficult puzzles
        """
        if self.__sudoku == None:
            return
        

        changed = True
        while changed:
            changed = False
            possible = [[[] for _ in range(9)] for _ in range(9)]
            srt = None

            for i in range(9):
                for j in range(9):
                    if self.__sudoku[i][j] == 0:
                        nums = [x for x in range(1,10)]
                        nums1 = [x for x in range(1,10)]
                        nums2 = [x for x in range(1,10)]
                        nums3 = [x for x in range(1,10)]
                        for k in range(9):
                            if self.__sudoku[i][k] in nums:
                                nums.remove(self.__sudoku[i][k])
                            if self.__sudoku[k][j] in nums:
                                nums.remove(self.__sudoku[k][j])
                            try:
                                if self.__sudoku[i][k] > 0:
                                    nums1.remove(self.__sudoku[i][k])
                                if self.__sudoku[k][j] > 0:
                                    nums2.remove(self.__sudoku[k][j])
                            except:
                                return 

                        sqi = (i//3)*3
                        sqj = (j//3)*3
                        for k in range(3):
                            for h in range(3):
                                if self.__sudoku[sqi+k][sqj+h] in nums:
                                    nums.remove(self.__sudoku[sqi+k][sqj+h])
                                try:
                                    if self.__sudoku[sqi+k][sqj+h] > 0:
                                        nums3.remove(self.__sudoku[sqi+k][sqj+h])
                                except:
                                    return
                        
                        if len(nums) == 1:
                            self.__sudoku[i][j] = nums[0]
                            
                                
                            changed = True
                        else:
                            possible[i][j] = nums
                            if srt == None:
                                srt = i,j
                            elif len(nums) < len(possible[srt[0]][srt[1]]):
                                srt = i,j
         

        if not self.is_actually_solved():            
            for p in possible[srt[0]][srt[1]]:
                
                s = [[self.__sudoku[i][j] for j in range(9)] for i in range(9)]
                s[srt[0]][srt[1]] = p
                sol = Sudoku_solver(s)
                sol.solve()
                
                
                if sol.is_actually_solved():
                    self.__sudoku = sol.get_solution()
                    break
            
        
        
        
        
                
                

        
        


            