#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 33.搜索旋转数组.py
@time   : 2019-12-04 14:55:02
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        if nums[0] <= target:
            #  在前半部分
            while left <= right:
                mid = left + (right - left) // 2  # 左边界
                if nums[mid] == target:
                    return mid
                elif nums[mid] < nums[0] or nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            # 在后半部分
            while left <= right:
                mid = left + (right - left) // 2  # 左边界
                if nums[mid] == target:
                    return mid
                elif nums[mid] > nums[-1] or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


print(Solution().search([6,8,9,1, 3,4,5], 8))
