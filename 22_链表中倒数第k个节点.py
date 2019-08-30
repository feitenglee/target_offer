#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 11:58:30
@LastEditTime: 2019-08-30 09:55:23
@Description: 双指针，快慢指针，类似的还有求链表的中间节点，
快指针每次走两步，慢指针每次走一步，快指针指向None，是慢指针
说指节点即为中间节点
@State: PYTHON35 PASS
'''
class Node():
    def __init__(self, data, p = None):
        self.data = data
        self.next = p

class Chain():
    def __init__(self):
        self.head = Node(None)
    def print(self):
        p = self.head.next#类内的变量需要self.
        while p != None:
            data = p.data
            p = p.next
            print(data,end='->')
        print("None")

'''
@discription: 找到链表倒数第k个数
@param {type} Node: 节点指针类型，k: int
@return: node.data: int
'''
def find_knode_to_tail(node,k):
    if not isinstance(node,Node) or not node:
        return None
    if not isinstance(k,int) or k <= 0:
        # print("k must be positive!")
        return None
    left = node
    right = left
    i = 0
    while i < k-1 and right.next != None:
        right = right.next
        i += 1
    if right.next == None:
        # print("k is larger than nums of Chain!")
        return None
    while right.next != None:
        left = left.next
        right = right.next
    return left.data
    

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(None)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    chain = Chain()
    chain.head.next = node1
    
    chain.print()
    print(find_knode_to_tail(node1,1))# 一般用例
    print(find_knode_to_tail(node1,3))# 一般用例
    print(find_knode_to_tail(node1,0))# 倒数第0个，不符合题意
    print(find_knode_to_tail(node1,6))# k超出链表个数
    print(find_knode_to_tail(node6,1))# 空链表，空节点
    
        

