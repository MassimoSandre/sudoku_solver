class Sudoku_solver:
    def __init__(self, sudoku=None):
        if sudoku == None:
            self.__sudoku = None
        self.__sudoku = [[sudoku[i][j] for j in range(9)] for i in range(9)]
        

    def set_sudoku(self, sudoku):
        self.__sudoku = sudoku
        

    def get_solution(self):
        return [[self.__sudoku[i][j] for j in range(9)] for i in range(9)]

    def print_sudoku(self):
        for l in self.__sudoku:
            for n in l:
                print(n,end=' ')
            print()

        print()

    def is_actually_solved(self):
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

    def solve(self):
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
                        for k in range(9):
                            if self.__sudoku[i][k] in nums:
                                nums.remove(self.__sudoku[i][k])
                            if self.__sudoku[k][j] in nums:
                                nums.remove(self.__sudoku[k][j])

                        sqi = (i//3)*3
                        sqj = (j//3)*3
                        for k in range(3):
                            for h in range(3):
                                if self.__sudoku[sqi+k][sqj+h] in nums:
                                    nums.remove(self.__sudoku[sqi+k][sqj+h])
                        
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
            
        
        
        
        
                
                

        
        


            