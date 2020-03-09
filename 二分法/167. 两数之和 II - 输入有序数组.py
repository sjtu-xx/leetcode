#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 167. 两数之和 II - 输入有序数组.py
@time   : 2019-12-04 17:32:04
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 直接查找target一定会超过时间
        # 因此，这里在找到target之后，在前面查找target的前一个数
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        # 找到target
        left = 0
        right = len(nums) - 1
        target_index = None
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                target_index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if target_index is None:
            return [-1, -1]
        else:
            # 寻找前半部分的界
            left = 0
            right = target_index
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                else:
                    left = mid + 1
            low_boundary = left

            print("hh")
            # 寻找后半部分的届
            left = target_index
            right = len(nums)
            while left < right:
                mid = left + (right - left + 1) // 2
                if nums[mid] == target:
                    left = mid
                else:
                    right = mid - 1
            high_boundary = left
            return [low_boundary, high_boundary]

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))