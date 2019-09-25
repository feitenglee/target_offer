#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 22:04:54
@LastEditTime: 2019-09-23 13:10:46
@Description: 
1、前序遍历
2、中序遍历
3、后序遍历
4、层序遍历
5、二叉树的右视图，层序遍历的变种
6、根据前序遍历和中序遍历重建二叉树
思路：队列中只存放下一层的所有节点，即pop出当前层的所有节点
@State: PYTHON35 PASS
'''
import sys
from queue import Queue#单向队列

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 前序遍历
# 1）递归实现
def pre_order(root):
    if root:
        print(root.data,end='->')
        pre_order(root.left)
        pre_order(root.right)
    # return 不返回任何值，仅仅是遍历二叉树
    
#2) 非递归实现1
def pre_order_recursive1(root):
    if not root:
        return
    stack = []
    p = root
    while p or stack:
        while p != None:
            print(p.data,end='->')
            stack.append(p)
            p = p.left
        if stack:
            p = stack.pop().right
            
#3) 非递归实现2
def pre_order_recursive2(root):
    if not root:
        return
    stack =[root]
    while stack:
        root = stack.pop()
        print(root.data,end='->')
        if root.right:
        # if root.right != None:
            stack.append(root.right)
        if root.left:
        # if root.left != None:
            stack.append(root.left)

# 中序遍历
# 1) 非递归
def in_order_recursive(root):
    if not root:
        return
    stack = []
    p = root
    while p or stack:
        if p:
            stack.append(p)
            # print(p.data, end='')
            p = p.left
        else:
            tmp = stack.pop()
            print(tmp.data, end='')
            p = p.right  
    print()

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
    print()

# 二叉树的右视图，将队列的最后一个元素保存下来
def right_view(root):
    if not isinstance(root, TreeNode):
        print("input is not TreeNode type!")
        sys.exit(1)
    if not root:
        return
    res = []
    q = [root]
    while q:
        res.append(q[-1].data)
        for _ in range(len(q)):# 加个for循环，每次队列中存放的都是下一层的所有节点
            node = q.pop(0) # pop出当前层的所有节点
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return  res

# 二叉树的左视图，与右视图相似，将队列的首个元素保存下来
def left_view(root):
    if not isinstance(root, TreeNode):
        print("input is not TreeNode type!")
        sys.exit(1)
    if not root:
        return
    res = []
    q = [root]
    while q:
        res.append(q[0].data)
        for _ in range(len(q)):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res
# 根据前序遍历和中序遍历重建二叉树
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
if __name__ == '__main__':
    """
            8
           /  \
          6   10
         / \   / \
        5   7 9  11
    """
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

    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    
    print("前序遍历：",end='')
    pre_order(node1)
    print("\n前序非递归遍历1：",end='')
    pre_order_recursive1(node1)
    print("\n前序非递归遍历2：",end='')
    pre_order_recursive2(node1)
    print("\n中序非递归遍历2：",end='')
    in_order_recursive(node1)
    print("\n层序遍历：",end='')
    level_order(node1)
    print("二叉树的右视图：",end='')
    print(right_view(node1))
    print("二叉树的左视图：",end='')
    print(left_view(node1))
    re_root = construct_BT(preorder,inorder)
    print("重建二叉树的前序遍历：",end='')
    pre_order(re_root)