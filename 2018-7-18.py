#709.To Lower Case
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str_list=list(str)
        str_len=len(str_list)
        for i in range(0,str_len):
            item_ascii=ord(str_list[i])
            if item_ascii<91 and item_ascii>64:
                str_list[i]=chr(ord(str_list[i])+32)
        str_low=''.join(str_list)
        return str_low
    def initialize():
        str='Hello'
        toLowerCase(self, str)

#771.Jewels and Stones
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_list=list(J)
        s_list=list(S)
        s_len=len(s_list)
        count=0
        for i in range(0,s_len):
            for items in j_list:
                if s_list[i] in items:
                    count+=1
        return count
    def initialize():
        J="aA"
        S = "aAAbbbb"
        numJewelsInStones(self,J, S)