#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 22:04:54
@LastEditTime: 2019-08-30 19:01:11
@Description: 
@State: PYTHON35 PASS
'''
import sys
from queue import Queue

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 前序遍历
def pre_order(root):
    if root:
        print(root.data,end='->')
        pre_order(root.left)
        pre_order(root.right)
    # return 不返回任何值，仅仅是遍历二叉树

# 层序遍历
def level_order(root):
    if not isinstance(root, TreeNode):
        print("input is not TreeNode type!")
        sys.exit(2)
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.data, end="->")
        
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

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

    pre_order(node1)
    print()
    level_order(node1)