#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 18:28:04
@LastEditTime: 2019-08-31 16:51:58
@Description: 队列，广度优先遍历，首先将根节点放到队列中，当队列不为空时，pop队首元素(访问且移除)，若左右节点不为空，将左右节点加入队列
2、分行打印，考虑本层未打印的个数和下一层带打印的个数
@State: PYTHON35 PASS
'''
import sys
from queue import Queue
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
def level_order(root):
    if not isinstance(root, TreeNode):
        print("input is not TreeNode type!")
        sys.exit(2)
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.data, end=" ")
        
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

# 将每一层分行打印       
def level_order2(root):
    if not isinstance(root, TreeNode):
        print("input is not TreeNode type!")
        sys.exit(2)
    q = Queue()
    q.put(root)
    to_be_print = 1
    next_level = 0
    while not q.empty():
        node = q.get()
        print(node.data, end=" ")
        to_be_print -= 1
        
        if node.left:
            next_level += 1
            q.put(node.left)
        if node.right:
            next_level += 1
            q.put(node.right)

        if to_be_print == 0:
            print()
            to_be_print = next_level
            next_level = 0
if __name__ == "__main__":
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(10)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(11)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7

    level_order(node1)
    p
    level_order2(node1)