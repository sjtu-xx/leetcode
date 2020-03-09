#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 861. 翻转矩阵后的得分.py
@time   : 2019-12-06 21:04:24
"""

from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        def reverse_line(i):
            A[i] = [not num for num in A[i]]

        # 先反转矩阵使得第一列全为1，然后反转后面的列，使得每一列都有较多的1
        height = len(A)
        width = len(A[0])
        for i in range(height):
            if A[i][0] != 1:
                reverse_line(i)
        score = 2**(width-1) * height
        for i in range(1,width):
            sum_col = sum([A[j][i] for j in range(height)])
            if sum_col>=(height+1)//2:
                score =score+ sum_col*(2**(width-1-i))
            else:
                score = score+ (height-sum_col)*(2**(width-1-i))
        return score
