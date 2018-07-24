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
                edge += 1 if n-1>=0 and grid[m][n - 1] else 0
                edge += 1 if n+1<length and grid[m][n + 1] else 0
                edge += 1 if m-1>=0 and grid[m - 1][n] else 0
                edge += 1 if m+1<width and grid[m + 1][n] else 0
    num=4*landnum-edge
    print num

grid=[[1]]
islandPerimeter(grid)
