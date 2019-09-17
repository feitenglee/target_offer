#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-06 09:41:30
@LastEditTime: 2019-09-06 10:21:53
@Description: 
题目1：两数之和问题
思路1：两重循环，时间复杂度O(n^2)
思路2：对于已经排序的数组，可以用首尾指针
题目2：和为s的连续整数数列
思路：同样是双指针，小于s，big指针++，大于s，small指针++
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

def find_continue_list_equal_s(s):
    if not isinstance(s, int):
        print("input is not int type")
        sys.exit(1)
    small, big = 1, 2
    res = []
    while small <= s // 2:
        if sequence_sum(small, big) < s:
            big += 1
        elif sequence_sum(small, big) > s:
            small += 1
        else:
            res.append([x for x in range(small, big+1)])
            small += 1
    return res
    
def sequence_sum(l, r):
    return (l+r)*(r-l+1)/2
if __name__ == "__main__":
    lis = [1,2,4,7,11,15]
    # print(two_sum(lis,15))
    # print(sequence_sum(1,4))
    print(find_continue_list_equal_s(15))