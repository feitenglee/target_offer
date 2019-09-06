#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-06 09:41:30
@LastEditTime: 2019-09-06 10:00:13
@Description: 
题目1：两数之和问题
思路1：两重循环，时间复杂度O(n^2)
思路2：对于已经排序的数组，可以用首尾指针
题目2：
@State: PYTHON35 PASS
'''
import sys

def two_sum(lis, s):
    if not isinstance(lis, list) or not isinstance(s, int):
        print("input is not list/int type")
        sys.exit(1)
    l, r = 0, len(lis)-1
    res = []
    while l < r:
        twosum = lis[l] + lis[r]
        if twosum < s:
            l += 1
        elif twosum > s:
            r -= 1
        else:
            res.append(lis[l])
            res.append(lis[r])
            break
    return res
    # print("lis has no two nums which sum is equal to given s!")
    # sys.exit(1)

if __name__ == "__main__":
    lis = [1,2,4,7,11,15]
    print(two_sum(lis,15))