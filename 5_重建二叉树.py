#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-23 09:51:53
@LastEditTime: 2019-09-23 10:35:41
@Description: 根据前序和中序遍历重建二叉树
@State: PYTHON35 PASS
'''
import sys
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def construct_BT(lis1,lis2):
    if not isinstance(lis1,list) or not isinstance(lis2,list):
        print("input is not list type!")
        sys.exit(2)
    if not lis1 or not lis2:
        return None
    if set(lis1) != set(lis2): # 判断两个序列是否匹配，元素是否相同
        return 
    root = TreeNode(lis1[0]) #根节点
    i = lis2.index(root.data)
    root.left = construct_BT(lis1[1:i+1],lis2[:i])
    root.right = construct_BT(lis1[i+1:],lis2[i+1:])
    return root

def pre_order(root):
    if not root:
        return
    print(root.data,end=' ')
    pre_order(root.left)
    pre_order(root.right)
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)
if __name__ == '__main__':
    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    re_root = construct_BT(preorder,inorder)
    print("重建后的前序遍历:",end='')
    pre_order(re_root)
    print("\n重建后的中序遍历:",end='')
    in_order(re_root)