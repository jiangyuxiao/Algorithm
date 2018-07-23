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
                if n-1>=0:
                    if grid[m][n - 1]:
                        edge += 1
                if n+1<length:
                    if grid[m][n + 1]:
                        edge += 1
                if m-1>=0:
                    if grid[m - 1][n]:
                        edge += 1
                if m+1<width:
                    if grid[m + 1][n]:
                        edge += 1
    num=4*landnum-edge
    print num
grid=[[0,1]]
islandPerimeter(grid)
