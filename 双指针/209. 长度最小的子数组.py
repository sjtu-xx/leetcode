#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 209. 长度最小的子数组.py
@time   : 2019-12-06 19:40:32
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = 0
        sum_s = 0
        for i in range(n):
            if sum_s < s:
                sum_s += nums[i]
                min_len += 1
            while sum_s > s:
                sum_s
                min_len -=1
                sum_s -= 1
        return False