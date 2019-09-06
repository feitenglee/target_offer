#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-03 19:55:38
@LastEditTime: 2019-09-03 20:16:33
@Description: 
思路1：辅助数，一个是累加的子数组和，一个是最大的子数组和
->1:累加的子数组和<0，字数组和置0
->2:比较字数组和 与 之前保存的最大子数组和，取最大值幅值给最大的子数组和
@State: PYTHON35 PASS
'''

import sys

def max_sum_subarray(lis):
    if not isinstance(lis, list):
        print("input is not list type")
        sys.exit(1)
    if not lis:
        return 0
    
    sub_sum = 0
    max_sum = 0
    for i in range(len(lis)):
        sub_sum += lis[i]
        if sub_sum < 0:
            sub_sum = 0
        # if sub_sum < 0:
        #     sub_sum = lis[i]
        # else:
        #     sub_sum += lis[i]
        max_sum = max(sub_sum, max_sum)
    return max_sum

if __name__ == "__main__":
    lis = [1,-2,3,10,-4,7,2,-5]#18
    lis1 = [1,2,3,10,-4,7,2,-5]#21
    print(max_sum_subarray(lis))
    print(max_sum_subarray(lis1))