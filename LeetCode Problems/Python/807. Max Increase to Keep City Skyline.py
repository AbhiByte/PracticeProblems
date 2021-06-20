def maxIncreaseKeepingSkyline(grid):
    max_front_view = 0
    max_side_view = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #For front/back view:
            if grid[i][j] > max_front_view:
                max_front_view = grid[i][j]
            if grid[i][j] > max_side_view:
                max_side_view = grid[i][j]
    print(max_front_view, max_side_view)

grider = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
maxIncreaseKeepingSkyline(grider)
