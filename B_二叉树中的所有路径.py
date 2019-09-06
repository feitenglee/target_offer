#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-01 15:16:35
@LastEditTime: 2019-09-01 16:59:40
@Description: 返回二叉树中所有的路径
@State: PYTHON35 PASS
'''
import sys

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def tree_path(root):
    '''
    @discription: 路径用字符串表示，也可以用列表表示
    @param {type} 
    @return: list
    ''' 
    str1 = ""
    res = []

    if not root:
        return []
    if not root.left and not root.right:
        str1 += str(root.data)
        # return res.append(str1)
        res.append(str1)
        return res

    left_lis = tree_path(root.left)
    
    for x in left_lis:
        res.append(str(root.data) + x)
 
    right_lis = tree_path(root.right)
    for y in right_lis:
        res.append(str(root.data) + y)
    return res

def tree_path2(root):
    # 路径用列表表示,不容易表示，需要解决[2],[[2,3]]这种问题，取元素不好取
    lis = []
    res = []
    if not root:
        return []
    if not root.left and not root.right:
        lis.append(root.data)
        res.append(lis)
        return res
    left_lis = tree_path2(root.left)
    for x in left_lis:
        tmp = ''
        tmp.join([str(y) for y in x])
        res.append(int(str(root.data) + tmp))
    
    right_lis = tree_path2(root.right)
    for x in right_lis:
        tmp = ''
        tmp.join([str(y) for y in x])
        res.append(int(str(root.data) + tmp))
    return res
if __name__ == "__main__":

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left,node1.right = node2,node3
    node2.left = node4
    node3.left,node3.right = node5,node6
    
    lis1 = tree_path(node1)
    # lis2 = tree_path2(node1)
    print(lis1)
    # print(lis2)
