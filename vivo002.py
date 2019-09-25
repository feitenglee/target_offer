#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-22 16:16:20
@LastEditTime: 2019-09-22 21:37:49
@Description: 
@State: PYTHON35 PASS
'''
# 002
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
   
def main(n, m):
    if n < 1 or m < 1:
        return -1
    head = Node(1)
    p = head
    #构造一个环形链表
    for i in range(2,n+1):
        tmp = Node(i)
        p.next = tmp
        p = tmp
    p.next = head

    p = p.next # p = head
    res = []
    while n > 0:
        for i in range(m-1):
            p = p.next
        res.append(p.data)
        tmp = p.next
        p.data, p.next = tmp.data, tmp.next
        n -= 1
    for x in res:
        print(x, end=" ")
    return res    
            
if __name__ == "__main__":
    str1,str2 = input("").split()
    n,m = int(str1),int(str2)
    main(n,m)