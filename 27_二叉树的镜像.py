#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 11:38:33
@LastEditTime: 2019-08-30 15:17:17
@Description: 二叉树遍历的变种,镜像即交换左右节点
@State: PYTHON35 PASS
'''
import sys
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def mirror_tree(root):
    if root:#非叶子节点
        root.left, root.right = root.right, root.left
        mirror_tree(root.left)
        mirror_tree(root.right)


def pre_order(root,lis1):
    if root:
        print(root.data,end='->')
        # lis1.append(root.data) #将遍历元素存储起来
        pre_order(root.left,lis1)
        pre_order(root.right,lis1)
        
def save_tree(root, lis1):
    pre_order(root,lis1)
    print(lis1)
    return lis1
if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(10)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(11)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.left,node3.right = node6,node7

    lis1 = []
    pre_order(node1,lis1)
    print(lis1)

    # mirror_tree(node1)
    # lis2 = pre_order(node1)
    # print(lis2)
