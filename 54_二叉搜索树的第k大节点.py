#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 20:41:15
@LastEditTime: 2019-09-05 20:54:16
@Description: 二叉树的中序遍历，是二叉树的升序
@State: PYTHON35 PASS
'''
import sys
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def kth_biggest_node(root, k):
    if not isinstance(root, TreeNode) or not isinstance(k,int):
        print("input is not TreeNode or int type!")
        sys.exit(1)
    if not root:
        print("root is Node")
        sys.exit(1)
    # if 
    lis = []
    mid_order(root,lis)
    if k >= len(lis):
        print("k is larger than the number of nodes")
        sys.exit(1)
    index = -1 * k
    return lis[-1*k]
def mid_order(root, lis):
    if not root:
        return
    if root:
        mid_order(root.left,lis)
        lis.append(root.data)
        mid_order(root.right,lis)
        
if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(7)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node7 = TreeNode(8)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.left,node3.right = node6,node7

    lis = []
    mid_order(node1,lis)
    print(lis)
    print(kth_biggest_node(node1,5))
    print(kth_biggest_node(node1,10))# k超出节点个数