#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 43. 字符串相乘.py
@time   : 2019-12-04 20:04:49
"""

from typing import List


class Solution:
    def multiply_one_char(self, num1_list: List[int], num2: int) -> List[int]:
        result_len = len(num1_list) + 1
        num1_list = [0] + num1_list
        result = [0] * result_len
        remainder = 0
        for i in range(result_len - 1, -1, -1):
            sub_result = num1_list[i] * num2 + remainder
            result[i] = sub_result % 10
            remainder = sub_result // 10
        return result

    def list_sum(self, num_list: List[List[int]], result):
        remainder = 0
        for i in range(len(num_list[0]) - 1, -1, -1):
            subresult = sum([num_l[i] for num_l in num_list]) + remainder
            result[i] = subresult % 10
            remainder = subresult // 10

    def multiply(self, num1: str, num2: str) -> str:
        num1_list, num2_list = list(map(int, num1)), list(map(int, num2))
        len_num1, len_num2 = len(num1), len(num2)
        max_result_len = len_num1 + len_num2 + 1
        result = [0] * max_result_len
        sub_result_list = []
        for i, v in enumerate(num2_list):
            sub_result_list.append(
                [0] * (i + 1) + self.multiply_one_char(num1_list, v) + [0] * (max_result_len - len_num1 - 2 - i))
        print(sub_result_list)
        self.list_sum(sub_result_list, result)
        for i in range(max_result_len):
            if result[i] != 0:
                return "".join(map(str, result[i:]))
        return "0"


print(Solution().multiply("0", "456"))
