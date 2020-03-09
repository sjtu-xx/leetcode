#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 162.寻找峰值.py
@time   : 2019-12-05 20:33:18
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 二分查找
        # 如果mid对应的数处于下坡阶段，则在左半区查找
        # 如果mid对应的数处于上坡阶段，则在右半区查找
        nums = [-float('inf')] + nums + [-float('inf')]
        L = len(nums)

        left = 1
        right = L - 2
        while left < right:
            mid = left + (right - left) // 2  # 左边界
            if nums[mid] < nums[mid + 1]:
                # 上坡阶段
                left = mid + 1
            elif nums[mid + 1] < nums[mid]:
                # 下坡阶段
                right = mid
        return left - 1


if __name__ == '__main__':
    print(Solution().findPeakElement([0]))
