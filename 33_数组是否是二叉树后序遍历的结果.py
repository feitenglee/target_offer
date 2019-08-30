#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 19:28:55
@LastEditTime: 2019-08-30 19:42:28
@Description: 后序遍历的特点：根节点在列表的末尾，且根据二叉树右子树比左子树大的特点，将前面元素分为左右子树，并递归下去。
@State: PYTHON35 PASS
'''
import sys

def is_post_order(lis):
    if not isinstance(lis, list):
        print("input is not list type!")
        sys.exit(2)
    root = lis[-1]
    index = 0
    for num in lis:
        if num < root:
            index += 1
        break
    is_post_order(left_part)
    is_post_order(right_part)
