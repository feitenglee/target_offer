#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 14:57:34
@LastEditTime: 2019-08-29 20:28:42
@Description: 
@State: PYTHON35 PASS 直链未通过
'''
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def meeting_node(node):
    slow = node
    fast = slow.next
    while fast.next != None and fast != slow:
        # if fast.next.next == None:
        #     return Node()
        fast = fast.next.next
        slow = slow.next
    if fast.next == None:# 直链情况
        print("this is not a loop chain!")
        return Node()
    return fast

def entry_node(node):
    if not isinstance(node,Node) or node.data == None:# 链表为空情况
        return Node()
    meet_node = meeting_node(node)
    if not meet_node:
        return Node()
    nodes_in_loop = 1
    p_node = meet_node
    while p_node.next != meet_node:#环内节点个数,与meet_node是否相遇，不是p_node
        p_node = p_node.next
        nodes_in_loop += 1
    left = node
    right = left
    for i in range(nodes_in_loop):
        right = right.next
    while left != right:
        left = left.next
        right = right.next
    return left

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
    # node6.next = node3 

    node7 = Node()  

    n1 = entry_node(node1)
    n2 = entry_node(node7)
    print(n1.data)
    print(n2.data)

