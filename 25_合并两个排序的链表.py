#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 11:15:01
@LastEditTime: 2019-08-30 11:36:15
@Description: 可看作递归问题，递归代码简洁，亦可迭代实现
@State: PYTHON35 PASS
'''
import sys

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
def merge_list(root1,root2):
    if not isinstance(root1,Node) and not isinstance(root2,Node):
        print("input is not Node type")
        sys.exit(1)
    if not root1:
        return root2
    if not root2:
        return root1
    head = None
    if root1.data <= root2.data:
        head = root1
        head.next = merge_list(root1.next, root2)
    else:
        head = root2
        head.next = merge_list(root1, root2.next)
    return head
    
def node_print(pHead):
        while pHead:
            print(pHead.data,end='->')
            pHead = pHead.next
        print("None")

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node_print(node1)

    node5 = Node(2)
    node6 = Node(4)
    node7 = Node(6)
    node8 = Node(8)
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node_print(node5)
    
    pHead = merge_list(node1,node5)
    node_print(pHead)

    node9 = None
    pHead2 = merge_list(node1,node9)
    node_print(pHead2)
    
    