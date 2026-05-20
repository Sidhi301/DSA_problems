class Solution(object):
    def isIsomorphic(self, s, t):
        dict1={}
        dict2={}
        for i,j in zip(s,t):
            if len(s)!=len(t):
                return False
            else:
                if (i not in dict1 or dict1[i]==j) and (j not in dict2 or dict2[j]==i) :
                    dict1[i]=j
                    dict2[j]=i
                else:
                    return False
        return True



        

      
        