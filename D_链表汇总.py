#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 09:34:25
@LastEditTime: 2019-09-17 10:06:01
@Description: 链表操作汇总
@State: PYTHON35 PASS
'''
import sys
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

        
# 删除链表第k个节点
def delete_node(head, k):
    if not isinstance(head, Node) or not isinstance(k, int):
        print("input is not Node or int type!")
        sys.exit(1)
    if k < 1:
        print("k must be positive!")
        sys.exit(1)
    p = head
    length = 0
    while p:
        length += 1
        p = p.next
    if k > length:
        print("k is larger than chain's length!")
        sys.exit()
    p = head
    for i in range(1,k):
        p = p.next
    tmp = p.next
    p.data, p.next = tmp.data, tmp.next
    
# 打印链表
def print_node(head):
    p = head
    while p:
        print(p.data,end='->')
        p = p.next
    print("None")
if __name__ == "__main__":
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

    print_node(node1)
    delete_node(node1,3)
    print_node(node1)
    
