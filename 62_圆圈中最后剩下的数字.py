#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 09:23:24
@LastEditTime: 2019-09-17 10:16:10
@Description: 环形链表模拟圆圈
@State: PYTHON35 PASS
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def last_remaining(n, m):
    if n < 1 or m < 1:
        return -1
    head = Node(0)
    p = head
    #构造一个环形链表
    for i in range(1,n):
        tmp = Node(i)
        p.next = tmp
        p = tmp
    p.next = head

    p = head
    while n > 1:
        for i in range(1,m):
            p = p.next
        tmp = p.next
        p.data, p.next = tmp.data, tmp.next
        n -= 1
    return p.data

if __name__ == "__main__":
    print(last_remaining(5,3))
    print(last_remaining(100,5))
        