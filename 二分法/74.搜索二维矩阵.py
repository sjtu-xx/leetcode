#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 74.搜索二维矩阵.py
@time   : 2019-12-04 17:05:41
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # 一定不存在的情况
        # if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
        #     return False
        #
        # # 可能存在的情况
        # width = len(matrix[0])
        # height = len(matrix)
        # # 在第一列中查找小于target的最大值
        # first_col_data = [matrix[i][0] for i in range(height)]
        # left = 0
        # right = height - 1
        # while left < right:
        #     mid = left + (right - left + 1) // 2
        #     if first_col_data[mid] > target:
        #         right = mid - 1
        #     elif first_col_data[mid] == target:
        #         return True
        #     else:
        #         left = mid
        #
        # # 在left行查找
        # lleft = 0
        # lright = width - 1
        # while lleft <= lright:
        #     mid = lleft + (lright - lleft) // 2
        #     if matrix[left][mid] == target:
        #         return True
        #     elif matrix[left][mid] > target:
        #         lright = mid - 1
        #     else:
        #         lleft = mid + 1
        # return False

        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        width = len(matrix[0])
        height = len(matrix)

        left = 0
        right = width * height - 1
        while left <= right:
            mid = left + (right - left) //2
            if matrix[mid//width][mid%width] == target:
                return True
            elif matrix[mid//width][mid%width] > target:
                right = mid -1
            else:
                left = mid + 1
        return False

print(Solution().searchMatrix(matrix=[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], target=3))
