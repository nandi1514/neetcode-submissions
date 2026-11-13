class Solution:
    
        
    def hasDuplicate(self, nums: List[int]) -> bool:
        def sortarray(nums):
            n = len(nums)
            for i in range(1, n):
                element =  nums[i]
                j = i-1
                while j>=0 and nums[j] > element:
                    nums[j+1] = nums[j]
                    j = j-1
                nums[j+1] = element

        sortarray(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False