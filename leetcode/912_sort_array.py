# https://leetcode.com/problems/sort-an-array/

class Solution:
    def mergeSort(self, nums: list[int]) -> list[int]:
        list_length = len(nums)

        if list_length == 1:
            return nums

        list1 = nums[:list_length//2]
        list2 = nums[list_length//2:]

        list1 = self.mergeSort(list1)
        list2 = self.mergeSort(list2)

        return self.merge(list1, list2)

    def merge(self, list1: list[int], list2: list[int]) -> list[int]:
        sorted_list = []

        while len(list1) != 0 and len(list2) != 0:
            if list1[0] < list2[0]:
                sorted_list.append(list1.pop(0))
            else:
                sorted_list.append(list2.pop(0))

        while len(list1) != 0:
            sorted_list.append(list1.pop(0))

        while len(list2) != 0:
            sorted_list.append(list2.pop(0))

        return sorted_list
