#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 15:05:00
@LastEditTime: 2019-08-30 15:20:12
@Description: 与26题树的子结构类似,递归比较左节点与右节点，右节点与左节点是否相等
@State: PYTHON35 PASS
'''
import sys

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_symmetric(root):
    if not isinstance(root, TreeNode):
        return False
    return comp_left_right(root,root)

def comp_left_right(root1, root2):
    if not root1 and not root2:# 两个节点都为空，说明已经遍历完
        return True
    if root1.data != root2.data:
        return False
    if not root1 or not root2: # 两节点不都为空，且一个节点为空，
        return False
    return comp_left_right(root1.left, root2.right) and \
           comp_left_right(root1.right, root2.left)

def pre_order(root):
    if root:
        print(root.data,end=' ')
        pre_order(root.left)
        pre_order(root.right)

if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(6)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(7)
    node7 = TreeNode(5)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.left,node3.right = node6,node7
    # node3.left = node6

    pre_order(node1)
    print()

    print(is_symmetric(node1))