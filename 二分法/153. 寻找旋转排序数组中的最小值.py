#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 153. 寻找旋转排序数组中的最小值.py
@time   : 2019-12-04 15:29:14
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        if nums[0] <= nums[-1]:
            # 递增序列
            return nums[0]

        left = 0
        right = len(nums) - 1
        # 旋转或递减序列
        while left < right:
            mid = left + (right - left) // 2  # 左边界
            if nums[mid] < nums[0]:
                right = mid
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                return nums[0] if nums[0] < nums[1] else nums[1]
        return nums[left]


print(Solution().findMin([2, 3, 4]))
