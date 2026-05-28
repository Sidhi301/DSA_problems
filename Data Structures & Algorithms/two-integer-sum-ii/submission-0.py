class Solution(object):
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        sum1=0
        while l<=r:
            sum1=numbers[l]+numbers[r]
            if sum1==target:
                return [l+1,r+1]
            else:
                if sum1>target:
                    r-=1
                else:
                    l+=1
                    

        





        
       
        
