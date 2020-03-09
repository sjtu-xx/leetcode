#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 174.地下城游戏.py
@time   : 2019-12-06 15:10:15
"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height = len(dungeon)
        width = len(dungeon[0])

        # 从curpos到第二排所有位置的最短距离
        sum_line = []
        for i in range(height):
            tmp = [dungeon[i][0]] + [0] * (width - 1)
            for j in range(1, width):
                tmp[j] = tmp[j - 1] + dungeon[i][j]
            sum_line.append(tmp)

        mini_blood = dungeon.copy()
        mini_blood[0] = sum_line[0]
        for i in range(1, height):
            for j in range(width):
                # 从第i-1行到达i行的第j个位置有j种方法
                possible_blood = [0] * (j+1)
                for k in range(j+1):
                    possible_blood[k] = sum_line[i - 1][k] + sum_line[i][i] - (sum_line[i][k - 1] if k - 1 > 0 else 0)
                mini_blood[i][j] = max(possible_blood)
        return mini_blood[-1][-1]

if __name__ == '__main__':
    print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))