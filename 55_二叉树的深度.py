#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 20:56:57
@LastEditTime: 2019-09-06 09:32:44
@Description: 二叉树的深度, 判断是否是平衡二叉树
题目1：二叉树深度
思路1：深度是max(左子树，右子树)+1，递归解决
题目2：是否是平衡二叉树
思路：不太理解
@State: PYTHON35 PASS
'''
import sys

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
#题目1：二叉树深度
def depth_of_tree(root):
    # if not isinstance(root, TreeNode):
    #     print("input is not TreeNode!")
    #     sys.exit(1)
    if not root:# 叶节点不是空，叶节点的子节点为空
        return 0
    left_depth, right_depth = 0, 0
    left_depth += depth_of_tree(root.left)
    right_depth += depth_of_tree(root.right)
    depth = max(left_depth, right_depth) + 1
    return depth

#题目2：判断是否是平衡二叉树，不太理解
def is_balanced(root):
    depth = 0
    return is_balanced_core(root, depth)

def is_balanced_core(root, depth):
    if not root:
        depth = 0
        return True
    left, right = 0, 0
    if is_balanced_core(root.left, left) and is_balanced_core(root.right, right):
        diff = left - right
        if abs(diff) <= 1:
            depth = max(left, right) + 1
            return True
    return False

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.right = node6
    node5.left = node7
    print(depth_of_tree(node1))
    print(is_balanced(node1))