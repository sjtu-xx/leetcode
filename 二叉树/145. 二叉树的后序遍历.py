#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 145. 二叉树的后序遍历.py
@time   : 2019-12-07 13:04:18
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def last_order(node):
            if node is None:
                return
            yield from last_order(node.right)
            yield node.val
            yield from last_order(node.left)

        gen = last_order(root)
        result = []
        while next(gen):
            result.append(next(gen))
        return result

