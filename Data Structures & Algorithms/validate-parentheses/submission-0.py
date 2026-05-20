class Solution(object): 
    def isValid(self, s):
        l1=[]
        dict1={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in s:
            if i in "({[":
                l1.append(i)
            else:
                if   not  l1  or l1[-1]!=dict1[i]:
                    return False
                l1.pop()
            
        return len(l1)==0
        


                



        