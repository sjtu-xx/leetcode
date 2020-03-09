#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 12.整数转罗马数字.py
@time   : 2019-12-04 23:25:12
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        def get_roman(quotient, divisor=100):
            ref_roman_char = roman_str[roman_char_dict[divisor]]
            ref_five_char = roman_str[roman_char_dict[divisor] + 1]
            ref_ten_char = roman_str[roman_char_dict[divisor] + 2]
            if quotient == 0:
                return ""
            elif quotient >= 1 and quotient <= 3:
                return ref_roman_char * quotient
            elif quotient == 4:
                return ref_roman_char + ref_five_char
            elif quotient <= 8:
                return ref_five_char + ref_roman_char * (quotient % 5)
            else:
                return ref_roman_char + ref_ten_char

        roman_char_dict = {j: i for i, j in enumerate([1, 5, 10, 50, 100, 500, 1000])}
        roman_str = "IVXLCDM"
        # 对于千位由于不存在更高位需要单独判断
        # 对于其他位，分为几种情况[1,3] [4] [5,8] [9]
        result = ""
        thousand = num // 1000
        if thousand > 0:
            result += roman_str[roman_char_dict[1000]] * thousand

        remainder = num % 1000
        for i in [100, 10, 1]:
            result += get_roman(remainder // i, i)
            remainder = remainder % i
        return result


print(Solution().intToRoman(1994))
