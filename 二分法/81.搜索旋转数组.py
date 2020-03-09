#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 81.搜索旋转数组.py
@time   : 2019-12-04 16:10:03
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 这类问题需要先判断在前半部分找，还是后半部分
        # 如果出现1111101的情况，需要（1）如果nums[0]==target返回True（2）left+=1 消除掉一个重复的元素
        # 然后在判断出现在前半部分还是后半部分
        if not nums:
            return False
        len_nums = len(nums)

        left = 0
        right = len_nums - 1
        if nums[left] == nums[right]:
            # 如果出现1111101的情况，预处理删除重复的值
            if nums[left] == target:
                return True
            else:
                while True:
                    left = min(left + 1, right)
                    if left == right:
                        return False
                    if nums[left] != nums[right]:
                        break

        if target == nums[left]:
            return True
        elif target > nums[left]:
            # 在前半段
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target or nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            assert (target < nums[left])
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target or nums[mid] > nums[right]:
                    left = target + 1
                else:
                    right = target - 1
        return False


print(Solution().search([1, 2, 3, 1, 1, 1], 3))
