#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 52.N皇后问题II.py
@time   : 2019-12-05 17:23:23
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        解题思路：可以理解为一个坐标系，0，0是原点，N*N里面的每个点有两个函数，斜率分别是1，-1，（y=-x+b, y=-x+b）xy_sum中记录的是y=x+b里面
        的b xy_dif记录的是y=-x+b里面的b 如果之后的点里面有相同的元素在这两个列表里面就说明在这条线上已经有另一个皇后在了。
        :param n:
        :return:
        """
        def get_pos(cur_pos, y_sub_x, y_add_x):
            len_c = len(cur_pos)
            # 当目前结果的长度达到n时，将得到的结果加入到result
            if len_c == n:
                result.append(cur_pos)
                return

            # 对于每一行
            for i in range(n):
                if i not in cur_pos and len_c - i not in y_sub_x and len_c + i not in y_add_x:
                    # 注意不能直接更改cur_pos，因为下次循环会遇到
                    get_pos(cur_pos+[i], y_sub_x+[len_c-i], y_add_x+[len_c+i])

        result = []
        get_pos([], [], [])
        return len(result)


if __name__ == '__main__':
    Solution().totalNQueens(4)
