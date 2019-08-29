#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 20:24:04
@LastEditTime: 2019-08-29 20:58:48
@Description: 反转链表
@State: PYTHON35 PASS 节点 指针
'''
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse_list(node):
    

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
    pReversedHead = reverse_list(node1)

    while pReversedHead:
        print(pReversedHead.data,end=' ')
        pReversedHead = pReversedHead.next