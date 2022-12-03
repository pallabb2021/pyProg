import time
import sys
import numpy as np

# grid = [[5,3,0,0,7,0,0,0,0],
#         [6,0,0,1,9,5,0,0,0],
#         [0,9,8,0,0,0,0,6,0],
#         [8,0,0,0,6,0,0,0,3],
#         [4,0,0,8,0,3,0,0,1],
#         [7,0,0,0,2,0,0,0,6],
#         [0,6,0,0,0,0,2,8,0],
#         [0,0,0,4,1,9,0,0,5],
#         [0,0,0,0,8,0,0,7,9]]
start = time.time()
grid =  [
    [0,9,0,0,0,7,0,0,8],
    [0,0,7,0,0,0,0,0,0],
    [0,0,0,8,0,3,9,1,0],
    [6,1,2,0,0,8,3,0,0],
    [0,0,0,0,0,0,0,6,0],
    [0,0,0,0,0,0,0,2,0],
    [4,0,0,0,8,0,2,0,0],
    [0,0,1,0,0,6,0,0,0],
    [0,7,0,4,0,0,0,0,1],
]
print(np.matrix(grid))

def possible(x,y,n):
    # check for a cell all the rows.
    for i in range(9):
        if grid[x][i] == n:
            print(f"Row check failed for i, (x,y) {i, (x,y)}")
            return False
    # check for a cell all the columns..
    for i in range(9):
        if grid[i][y] == n:
            print(f"Column check failed for i, (x,y) {i, (x, y)}")
            return False
    # check the 3 X 3 grid
    gridx_3X3= (x//3)*3
    gridy_3X3 =(y//3)*3

    for i in range(3):
        for j in range(3):
            if grid[gridx_3X3+i][gridy_3X3+j] == n:
                print(f"(x,y) has grid {(x, y), gridx_3X3+i, gridy_3X3+j}")
                return False
    return True
    """
    00(0, 0) 01 02 
    10 	 11 12(0,0)
    20 	 21 22

    30(1,0) 31 32
    40 	41 42
    50 	51 52(1,0)
    """


def solve():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[x][y] = n
                        print("Solve called again")
                        solve()

                    grid[x][y] =0
                return
    print(np.matrix(grid))
    end= time.time()
    print(end-start)
    sys.exit(0)

solve()
