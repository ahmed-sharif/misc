


# http://www.geeksforgeeks.org/collect-maximum-points-in-a-grid-using-two-traversals/


grid = [
    [3, 6,  8,  2],
    [5, 2,  4,  3],
    [1, 1, 20, 10],
    [1, 1, 20, 10],
    [1, 1, 20, 10],
]


end_row = len(grid)/2
for row in range(len(grid)-1, end_row - 1, -1):
    for col in range(len(grid) - row + 1):
        maxval = 0
        if row + 1 < len(grid):
            if col - 1 >= 0:
                maxval = max(maxval, grid[row + 1][col - 1]
            maxval = max(maxval, grid[row+1][col]
