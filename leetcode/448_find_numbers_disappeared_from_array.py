# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        return [i for i, num in enumerate(nums, 1) if num > 0]