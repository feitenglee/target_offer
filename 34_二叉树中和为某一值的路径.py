#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-31 17:05:53
@LastEditTime: 2019-09-01 16:50:24
@Description: 
@State: PYTHON35 PASS
'''

import sys

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def find_path(root, val):
    if not isinstance(root, TreeNode) or not isinstance(val, int):
        print("inputs are not TreeNode or int type!")
        sys.exit(1)
    path = []
    cur_val = 0
    find_path2(root, val, path, cur_val)

def find_path2(node, val, path, cur_val):
    '''
    @discription: 
    @param {type} 
    @return: none 
    '''    
    cur_val += node.data
    path.append(node)
    # 叶子节点的条件 not node.left and not node.right
    if cur_val == val and not node.left and not node.right:
        for i in path:
            print(i.data, end=' ')
        print()
    if node.left:
        find_path2(node.left, val, path, cur_val)
    if node.right:
        find_path2(node.right, val, path, cur_val)
    path.pop()

# 递归判断是否包含和为某一值的路径（从根节点到叶子节点）
# 判断左右子树是否包含val-root.data值的路径，递归下去
def has_path_sum(root, val):
    # 这种递归终止条件包含单独根节点的路径，不符合题意
    # if not root:
    #     return val == 0
    
    if not root:
        return False
    if not root.left and not root.right:
        return root.data == val
    # 递归左右子树
    if (has_path_sum(root.left, val - root.data)):
        return True
    if (has_path_sum(root.right, val - root.data)):
        return True
    return False

if __name__ == "__main__":
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(12)
    node4 = TreeNode(4)
    node5 = TreeNode(7)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5

    find_path(node1,22)
    print(has_path_sum(node1, 22))