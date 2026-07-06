class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        m=len(nums)
        n=2*(len(nums))
        for i in range(n):
            j=i-m
            ans.append(nums[j])
        return ans
            
        
        