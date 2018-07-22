# 728. Self Dividing Numbers

def isSelfDividingNumbers(num):
    n=num
    m=num
    while m>0:
        n=m%10
        m=m//10
        if n==0 or num%n!=0:
            return 0
    return 1

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    selfDividingNumber=[]
    for num in range(left,right):
        if(isSelfDividingNumbers(num)):
            selfDividingNumber.append(num)
    print selfDividingNumber


def initialize():
    LowerNumberBound=1
    UpperNumberBound=22
    selfDividingNumbers(LowerNumberBound,UpperNumberBound+1)

initialize()