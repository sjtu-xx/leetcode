#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 60.第k个排列.py
@time   : 2019-12-04 20:51:41
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count_total = [1]
        for i in range(1, n):
            count_total.append(count_total[-1] * (i + 1))

        n_num = [i for i in range(1, n + 1)]
        result = []
        for i in range(n):
            quotient = k // count_total[n - 2 - i]
            k = k % count_total[n - 2 - i]
            if k == 0:
                result.append(n_num.pop(quotient - 1))
            else:
                result.append(n_num.pop(quotient))
        return "".join(map(str, result))


print(Solution().getPermutation(4, 9))
