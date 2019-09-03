#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-03 16:17:44
@LastEditTime: 2019-09-03 16:46:39
@Description: 
a)快排：
思路：前两步是partition过程，第三步是递归过程
->1: 选定第一个元素作为pivot, 遍历[l+1,r]的元素，将数组分为<v和>v的部分
->2: 交换l与j+1的元素，将v放在应该在的位置，返回此时v的索引。
->3: 对<v和>v的部分递归调用快排函数

@State: PYTHON35 PASS
'''
import sys
import random

def quick_sort(lis):
    if not isinstance(lis, list):
        print("input is not list type!")        
        sys.exit(1)
    if not lis:
        return 
    
    quick_sort_core(lis,0,len(lis)-1)

def quick_sort_core(lis, l, r):
    if l > r:# 递归出口
        return
    p = partition(lis, l, r)
    quick_sort_core(lis, l, p-1)
    quick_sort_core(lis, p+1, r)

def partition(lis, l, r):
    v = lis[l]
    j = l
    for i in range(l+1,r+1):
        if lis[i] < v:
            j += 1
            lis[j],lis[i] = lis[i],lis[j]
    lis[l],lis[j] = lis[j],lis[l]
    return j

if __name__ == "__main__":
    lis = [random.randint(0,10) for _ in range(10)]
    print(lis)
    quick_sort(lis)
    print(lis)