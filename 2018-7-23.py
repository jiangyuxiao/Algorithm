def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    landnum=0
    edge=0
    width=len(grid)
    length=len(grid[0])
    for m in range(0,width):
        for n in range(0,length):
            if grid[m][n]:
                landnum+=1
                if m==0:
                    if n==0:
                        if grid[m][n + 1]:
                            edge += 1
                        if grid[m + 1][n]:
                            edge += 1
                    elif n==length-1:
                        if grid[m][n - 1]:
                            edge += 1
                        if grid[m + 1][n]:
                            edge += 1
                    else:
                        if grid[m][n - 1]:
                            edge += 1
                        if grid[m][n + 1]:
                            edge += 1
                        if grid[m + 1][n]:
                            edge += 1
                elif m==width-1:
                    if n==0:
                        if grid[m][n + 1]:
                            edge += 1
                        if grid[m - 1][n]:
                            edge += 1
                    elif n==length-1:
                        if grid[m][n - 1]:
                            edge += 1
                        if grid[m - 1][n]:
                            edge += 1
                    else:
                        if grid[m][n - 1]:
                            edge += 1
                        if grid[m][n + 1]:
                            edge += 1
                        if grid[m - 1][n]:
                            edge += 1
                else:
                    if n==0:
                        if grid[m][n + 1]:
                            edge += 1
                        if grid[m - 1][n]:
                            edge += 1
                        if grid[m + 1][n]:
                            edge += 1
                    elif n==length-1:
                        if grid[m][n - 1]:
                            edge += 1
                        if grid[m - 1][n]:
                            edge += 1
                        if grid[m + 1][n]:
                            edge += 1
                    else:
                        if grid[m][n - 1]:
                            edge += 1
                        if grid[m][n + 1]:
                            edge += 1
                        if grid[m - 1][n]:
                            edge += 1
                        if grid[m + 1][n]:
                            edge += 1
    print 4*landnum-edge



grid=[[0,1,0,0,0],
      [1,1,1,0,0],
      [0,1,0,0,0],
      [1,1,0,0,0]]
islandPerimeter(grid)
