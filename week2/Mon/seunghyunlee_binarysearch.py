class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(logn) 
        
        nums = [-2**31-1] + nums + [-2**31-1]
        
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            
            a, b, c = nums[mid-1], nums[mid], nums[mid+1]
            
            if b>a and b>c:
                return mid-1
            
            elif c>b:
                start = mid+1
            
            else:
                end = mid-1