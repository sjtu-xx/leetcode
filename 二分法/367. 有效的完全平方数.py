#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 367. 有效的完全平方数.py
@time   : 2019-12-05 21:38:56
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = (left + right) // 2  # 左边界
            pow2_mid = mid ** 2
            if pow2_mid == num:
                return True
            elif pow2_mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    print(Solution().isPerfectSquare(5))
