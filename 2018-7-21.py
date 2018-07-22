#771.Jewels and Stones
def numJewelsInStones(J, S):
    j_list=list(J)

    s_dic={}
    s_list=list(S)
    s_len=len(s_list)
    for i in range(0,s_len):
        if s_dic.has_key(s_list[i]):
            s_dic[s_list[i]]+=1
        else:
            s_dic[s_list[i]]=1

    count=0
    for key,value in s_dic.items():
        if key in j_list:
            count+=int(value)
    print count


def initialize():
    J="aAcosU"
    S = "aAAbbbb"
    numJewelsInStones(J, S)

initialize()