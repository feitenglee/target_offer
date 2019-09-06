#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-01 11:33:10
@LastEditTime: 2019-09-01 18:50:20
@Description: 序列化的意思是将二叉树以文本的形式存储以来，反序列化是将文件还原成一个二叉树类型
@State: NO PASS
'''

import sys

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def serialize(root, lis):
    '''
    @discription: 序列化
    @param {type} 
    @return: lis 
    '''    
    if not root:
        lis.append("$")
    if root:
        lis.append(str(root.data))
        serialize(root.left, lis)
        serialize(root.right, lis)

def deserialize(lis):
    '''
    @discription: 反序列化
    @param {type} 
    @return: TreeNode
    '''
    tree, index = deserialize2(lis,0)
    return tree

def deserialize2(lis, index):
    '''
    @discription: 
    @param {type} 
    @return: TreeNode
    '''    
    if index > len(lis)-1:
        return None
    if not lis[index].isdigit():
        index = index + 1
    node = TreeNode(int(lis[index])) 
    index += 1
    node.left = deserialize2(lis, index)
    node.right = deserialize2(lis, index)
    return node


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

    lis1 = []
    serialize(node1,lis1)
    print(lis1)

    node = deserialize(lis1)
    # print(node.left.data)
