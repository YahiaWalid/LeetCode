#35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        
        n = len(nums)
        middle = n // 2

        if n == 0:
            return 0

        if nums[middle] == target:
            return middle

        if target < nums[middle]:
            return self.searchInsert(nums[:middle], target)
        else:
            return middle + 1 + self.searchInsert(nums[middle + 1:], target)


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 7))
