class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        dict1={}
        l1=[]
        if len(arr)==k:
            return arr
        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        dict2=sorted(dict1.items(),
                key=lambda x:x[1],
                reverse=True)
            
        res=[]
        for nums,val in dict2:
            res.append(nums)
        return res[:k]
        