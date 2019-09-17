#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-06 11:01:01
@LastEditTime: 2019-09-11 09:55:11
@Description: 
题目1：滑动窗口的最大值
思路1：两个指针，遍历每个窗口，把每个窗口的最大值加入到待返回的列表中，两个循环，时间复杂度为O(nk),k为窗口宽度
思路2：
@State: PYTHON35 PASS
'''
import sys
from collections import deque #双端队列
 
def max_in_window(lis,n):
    if not isinstance(lis, list) or not isinstance(n, int):
        print("input is not list or int type!")
        sys.exit(1)
    if n > len(lis):
        print("n is larger than the length of lis!")
        sys.exit(1)
    if n < 0:
        print("n must be not negative")
        sys.exit(1)
    if not lis:
        return []
    res = []
    l,r = 0,n-1
    while r <= len(lis)-1:
        max_val = lis[l]
        for i in range(l, r+1):
            if lis[i] > max_val:
                max_val = lis[i]
        res.append(max_val)
        l += 1
        r += 1
    return res

if __name__ == "__main__":
    lis = [2,3,4,2,6,2,5,1]
    print(max_in_window(lis,3))
 