#136. Single Number
class Solution(object):
    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int

        Given a non-empty array of integers nums, every element appears twice except for one.
        Find that single one.

        """


        count = {}


        for number in nums:
            count[number]= count.get(number,0)+1

        for number in nums:
            if count.get(number) == 1:
                return number

s = Solution()
result = s.singleNumber([2,2,1])
print(result)
