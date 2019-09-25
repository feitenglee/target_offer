#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 09:34:25
@LastEditTime: 2019-09-22 22:19:51
@Description: 链表操作汇总
1、删除单链表第k个节点
2、打印链表
3、环形链表
4、从尾到头打印链表
5、反转链表
6、
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

# 环形链表打印m的倍数个节点，m排序
def m_order(n, m):
    if n < 1 or m < 1:
        return -1
    head = Node(1)
    p = head
    #构造一个环形链表,从1开始到n
    for i in range(2,n+1):
        tmp = Node(i)
        p.next = tmp
        p = tmp
    p.next = head

    p = p.next # p 指向 head
    res = []
    while n > 0:
        for i in range(m-1):
            p = p.next
        res.append(p.data)
        tmp = p.next
        p.data, p.next = tmp.data, tmp.next#删除第m个节点
        n -= 1
    for x in res:
        print(x, end=" ")
    return res
def print_from_ceil(head):
    if not isinstance(head, Node):
        print("input is not Node type!")
        sys.exit(1)
    stack = [] # 列表构造一个栈
    p = head
    while p:
        stack.append(p)
        p = p.next
    while stack:
        tmp = stack.pop()
        print(tmp.data, end=' ')
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

    print("原链表：",end='')
    print_node(node1)
    delete_node(node1,3)
    print("删除第k个节点后的链表：",end='')
    print_node(node1)
    str1,str2 = input("请输入n和m:").split()
    n,m = int(str1),int(str2)
    print("m排序后的链表：",end='')
    m_order(n,m)
    print("\n从尾到头打印链表：",end='')
    print_from_ceil(node1)
