#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 807.保持城市天际线.py
@time   : 2019-12-05 17:11:21
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top_max = [max([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]
        left_max = [max(line) for line in grid]
        total_incre = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total_incre += min([left_max[i], top_max[j]]) - grid[i][j]
        return total_incre


if __name__ == '__main__':
    Solution().maxIncreaseKeepingSkyline(grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
