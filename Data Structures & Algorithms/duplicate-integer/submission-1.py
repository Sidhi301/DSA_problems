class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
        nums.sort()
        i=0
        j=1
        while(i<j and j<len(nums)):
            if nums[j]==nums[i]:
                return True
            i+=1
            j+=1;
        return False

        