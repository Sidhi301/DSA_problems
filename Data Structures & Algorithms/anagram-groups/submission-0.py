class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        l1=[]
        s=""
        for i in strs:
            s="".join(sorted(i))
            if s not in dict1:
                dict1[s]=[i]
            elif s in dict1:
                dict1[s].append(i)
        for j in dict1:
            l1.append(dict1[j])
        return l1




        