#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 415.字符串相加.py
@time   : 2019-12-04 19:44:36
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_list = list(map(int, num1))
        num2_list = list(map(int, num2))
        len_num1 = len(num1)
        len_num2 = len(num2)
        if len_num2 >= len_num1:
            max_result_length = len_num2 + 1
        else:
            max_result_length = len_num1 + 1
        num1_list = [0] * (max_result_length - len_num1) + num1_list
        num2_list = [0] * (max_result_length - len_num2) + num2_list

        result = [0] * max_result_length
        remainder = 0

        for i in range(max_result_length - 1, -1, -1):
            bit_sum = num1_list[i] + num2_list[i] + remainder
            result[i] = bit_sum % 10
            remainder = bit_sum // 10

        return "".join(map(str, result[1:])) if result[0] == 0 else "".join(map(str, result))