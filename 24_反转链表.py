#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 20:24:04
@LastEditTime: 2019-08-30 11:09:33
@Description: 反转链表，防止链表断裂，
@State: PYTHON35 PASS 节点 指针
'''
import sys

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse_list(node):
    if not isinstance(node,Node) or not node:
        print("Input is not Node type or node is empty")
        sys.exit(2)
    if node.next == None:
        return node

    pre = None
    cur = node
    next = None
    # 需要弄清楚条件是cur还是cur.next非空
    while cur:
        next = cur.next
        if cur.next == None:
            reverse_head = cur
        cur.next = pre
        
        pre = cur
        cur = next
    return reverse_head
        


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    tmp = node1
    while tmp:
        print(tmp.data,end='->')
        tmp = tmp.next
    print()

    pReversedHead = reverse_list(node1)
    
    while pReversedHead:
        print(pReversedHead.data,end='->')
        pReversedHead = pReversedHead.next