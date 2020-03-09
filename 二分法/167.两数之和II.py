#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 167.两数之和II.py
@time   : 2019-12-05 20:52:55
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 二分
        # n = len(numbers)
        # if n < 2:
        #     return []
        # for i in range(n - 1):
        #     num2 = target - numbers[i]
        #     if num2 < numbers[i + 1]:
        #         continue
        #     left = i + 1
        #     right = n - 1
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] == num2:
        #             return [i+1, mid+1]
        #         elif numbers[mid] > num2:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        # return []

        # 双指针法
        n = len(numbers)
        if n < 2:
            return []
        left = 0
        right = n - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1]
            elif two_sum > target:
                right -= 1
            else:
                left += 1
        return []


if __name__ == '__main__':
    print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
