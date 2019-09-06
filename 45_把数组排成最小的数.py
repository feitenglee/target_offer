#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 09:24:05
@LastEditTime: 2019-09-05 09:41:26
@Description: 输入一个正整数数组，把数组中所有数字拼接起来排成一个数，打印最小的那个数字
思路1：全排列，返回全排列中最小的数
思路2:重定义比较函数，python中cmp_to_key高级函数
@State: PYTHON35 PASS
'''
import sys
from functools import cmp_to_key

def find_min_combination(num):
    if not isinstance(num, list):
        print("input is not list type")
        sys.exit(1)
    if not num:
        return ""
    lmb = cmp_to_key(lambda n1,n2: int(str(n1)+str(n2)) - int(str(n2)+str(n1)))
    lis = sorted(num, key=lmb)
    return "".join([str(x) for x in lis])

if __name__ == "__main__":
    # lis = [3,32,321]
    lis = [1,2,3]
    print(find_min_combination(lis))