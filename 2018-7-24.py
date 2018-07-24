#463
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

#258
def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    def add(n):
        m=0
        for d in str(n):
           m+=int(d)
        if m<10:
            return m
        else:
            return add(m)
    print add(num)
num=59
addDigits(num)

#283
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nlen=len(nums)
    i=0
    m=nlen
    while i<m:
        if nums[i]!=0:
            i+=1
        else:
            for n in range(i,nlen-1):
                nums[n]=nums[n+1]
            nums[nlen-1]=0
            m-=1
    print nums
nums=[0,1,0,0,3,12]
moveZeroes(nums)
