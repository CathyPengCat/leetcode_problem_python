#/usr/bin/python3
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        index = 0
        for x in nums:
            if target-x in nums_dict:
                return nums_dict[target-x], index
            else:
                nums_dict[x] = index
            index += 1
