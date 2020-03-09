#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 230. 二叉搜索树中第K小的元素.py
@time   : 2019-12-06 18:55:14
"""

class Solution:
    def mid_order(self,node):
        if not node:
            return
        yield from self.mid_order(node.left)
        yield node.val
        yield from self.mid_order(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        gen = self.mid_order(root)
        for _ in range(k-1):
            next(gen)
        return next(gen)
