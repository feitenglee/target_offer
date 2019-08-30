#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 16:31:09
@LastEditTime: 2019-08-30 18:26:22
@Description: 栈的操作，突破口是如果辅助栈顶元素是待弹出元素，直接弹出，
若不是，继续压入直到栈顶元素与待弹出元素相等
@State: PYTHON35 PASS
'''

import sys

def is_pop(lis1, lis2):
    if not isinstance(lis1, list) or not isinstance(lis2, list):
        print("input is not list type!")
        sys.exit(2)
    if len(lis1) != len(lis2):
        print("arg1 and arg2 must have same length!")
        sys.exit(2)
    tmp = []
    index = 0
    # for i in range(lis1):
    # while tmp:
    #     if lis1[-1] != lis2[index]:
    #         tmp.append(lis1[i])
    #     index += 1
    for num in lis1:
        tmp.append(num)
        while tmp and tmp[-1] == lis2[index]:
            tmp.pop()
            index += 1
    if tmp:
        return False
    return True

if __name__ == "__main__":
    lis1 = [1,2,3,4,5]
    lis2 = [4,5,3,2,1]
    print(is_pop(lis1,lis2))