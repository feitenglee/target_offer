#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 19:28:55
@LastEditTime: 2019-08-31 16:53:16
@Description: 后序遍历的特点：根节点在列表的末尾，且根据二叉树右子树比左子树大的特点，将前面元素分为左右子树，并递归下去。
判断+循环：while
单纯循环： for
单纯判断： if
@State: PYTHON35 PASS
'''
import sys


def is_post_order(lis):
    '''
    @discription: 判断输入列表是否是某个二叉树后序遍历的结果
    @param {type} list
    @return: 返回是bool型，递归子函数也必须有返回值
    '''    
    if not isinstance(lis, list):
        print("input is not list type!")
        sys.exit(2)
    root = lis[-1]
    length = len(lis)
    i = 0
    while i < length - 1:
        if lis[i] > root:
            break
        i += 1                 
    j = i
    while j < length:
        if lis[j] < root:
            return  False
        j += 1
    left = True #递归出口/边界条件
    if i > 0:
        left = is_post_order(lis[:i])
    right = True
    if i < length -1:
        # right = is_post_order(lis[:length-1])
        # is_post_order(lis[:j])
        is_post_order(lis[:-1])
    return left and right

if __name__ == "__main__":
    lis = [5,7,6,9,11,10,8]
    lis2 = [7,4,6,5]
    print(is_post_order(lis))
    print(is_post_order(lis2))