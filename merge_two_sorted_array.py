#!/usr/bin/python3class Solution(object):
class Solution(object):
	def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #nums1[m:] = nums2
	#nums1.sort()
	end = m + n - 1
        idx1 = m-1
        idx2 = n-1
        while idx1 != -1 and idx2 != -1:
            if nums1[idx1] <= nums2[idx2]:
                nums1[end] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[end] = nums1[idx1]
                idx1 -= 1
            end -= 1
        if idx1 == -1:
            while idx2 != -1:
                nums1[end] = nums2[idx2]
                end -= 1
                idx2 -= 1

