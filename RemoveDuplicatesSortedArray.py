#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        for i in range (1,len(nums)):
            if nums [i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1

        return k


s = Solution()
sol = s.removeDuplicates([1,1,2,3,4])
print(sol)
