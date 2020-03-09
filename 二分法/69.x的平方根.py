#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 69.x的平方根.py
@time   : 2019-12-04 15:18:58
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x<0:
            return -1
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            pow2_mid = mid ** 2
            if pow2_mid == x:
                return mid
            elif pow2_mid < x:
                if (mid + 1) ** 2 > x:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1
        return -1

print(Solution().mySqrt(0))
