#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 154. 寻找旋转排序数组中的最小值 II.py
@time   : 2019-12-05 21:08:04
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 先判断旋转数组是否旋转，即是否分为两段：
        # 1。如果头元素与尾元素相同，删除重复的元素，直到与重复的元素不同
        # 2。如果头元素大于尾元素，则为旋转数组
        #    如果头元素小于尾元素，则第一个元素为最小值
        if not nums:
            return -1
        n = len(nums)
        left = 1
        right = n - 1
        while nums[left] == nums[0] and left < right:
            left += 1
        left = max(0, left - 1)

        if nums[left] < nums[right]:
            return left
        # 头元素大于或等于尾元素（等于尾元素时，left和right指向相同的数）
        while left < right:
            mid = left + (right - left) // 2  # 左边界
            if nums[mid] <= nums[right]:
                # 在右侧的数组中
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(Solution().findMin([2, 2, 2, 0, 1]))
