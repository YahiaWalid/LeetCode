#217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)

        for i in range(n):
            for j in range (i+1,n):
                if nums[i]==nums[j]:
                    return True
        return False


s = Solution()

print(s.containsDuplicate([1,2,3,1,1]))
