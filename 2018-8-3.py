#167
def twoSum1(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0,len(numbers)):
        m=target-numbers[i]
        if m in numbers:
            if m==numbers[i]:
                index1=i+1
                index2=i+2
                return [index1,index2]
            else:
                index1=i+1
                index2=numbers.index(m)+1
                return [index1,index2]

def twoSum2(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    low=0
    high=len(numbers)-1
    while low<=high:
        if numbers[low]+numbers[high]!=target:
            if numbers[low]+numbers[high]>target:
                high-=1
            elif numbers[low]+numbers[high]<target:
                low+=1
        else:
            index1=low+1
            index2=high+1
            return [index1,index2]

#169
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n_dic={}
    n_len=len(nums)
    for i in range(0,len(nums)):
        if n_dic.has_key(nums[i]):
            n_dic[nums[i]]+=1
        else:
            n_dic[nums[i]]=1
    for key,value in n_dic.items():
        if value>n_len/2:
            return key
