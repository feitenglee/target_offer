#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 14:57:34
@LastEditTime: 2019-08-30 11:08:42
@Description: 1、判断是否存在回环，2、回环内节点的个数 3、快慢指针相遇时为环的入口节点
@State: PYTHON35 PASS 
'''
import sys

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def meeting_node(node):
    
    slow = node
    fast = slow.next
    # 需要仔细考虑这里的判断条件
    while fast != None and fast.next != None and fast != slow:
        fast = fast.next.next
        slow = slow.next
    if fast == None or fast.next == None:# 直链情况
    # if not fast or fast.next == None:# 直链情况
        print("this is not a loop chain!")
        sys.exit(2)
    return fast

def entry_node(node):
    if not isinstance(node,Node) or not node:# 链表为空情况
        return None
    meet_node = meeting_node(node)
    if meet_node == None:
        return None
        
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
    node7 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    # node6.next = node3 

    node7 = Node()  

    n1 = entry_node(node1)
    # n2 = entry_node(node7)
    print(n1.data) # 返回None时，没有data属性
    # print(n2.data)

