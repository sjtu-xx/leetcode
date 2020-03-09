#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@project : leetcode
@author  : xuexuan
@file   : 222. 完全二叉树的节点个数.py
@time   : 2019-12-06 18:25:42
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 再来回顾一下满二叉的节点个数怎么计算，如果满二叉树的层数为h，则总节点数为：2^h - 1.
# 那么我们来对root节点的左右子树进行高度统计，分别记为left和right,有以下两种结果：

# 1.left == right。这说明，左子树一定是满二叉树，因为节点已经填充到右子树了，左子树必定已经填满了。所以左子树的节点总数我们可以直接得到，是2^left - 1，加上当前这个root节点，则正好是2^left。再对右子树进行递归统计。
# 2.left != right。说明此时最后一层不满，但倒数第二层已经满了，可以直接得到右子树的节点个数。同理，右子树节点+root节点，总数为2^right。再对左子树进行递归查找。


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # # 二叉树左右子树递归
        # if root is None:
        #     return 0
        # return self.countNodes(root.left)+self.countNodes(root.right)+1

        # 方法2
        if root is None:
            return 0

        def count_level(node):
            level = 0
            while node is not None:
                level += 1
                node = node.left
            return level

        count = 0
        left_level = count_level(root.left)
        right_level = count_level(root.right)
        if left_level == right_level:
            return self.countNodes(root.right) + 1 << left_level
        else:
            return self.countNodes(root.left) + 1 << right_level
