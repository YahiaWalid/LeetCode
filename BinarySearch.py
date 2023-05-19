#704. Binary Search


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        middle = n//2

        if n == 0:
            return -1

        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return self.search(nums[:middle], target)
        else:
            result = self.search(nums[middle+1:], target)
            if result == -1:
                return -1
            else:
                return middle + 1 + result




s = Solution()
sol = s.search([-1,0,3,5,9,12],12)
print(sol)
