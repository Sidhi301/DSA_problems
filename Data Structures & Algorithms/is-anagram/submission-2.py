class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        for i in range(len(s)):
            dict1[s[i]]=dict1.get(s[i],0)+1
        for ch in t:
            if  ch not in dict1 or dict1[ch]==0:
                return False
            dict1[ch]-=1
        return True
        