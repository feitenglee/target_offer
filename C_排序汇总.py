#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-03 16:17:44
@LastEditTime: 2019-09-05 16:42:59
@Description: 排序算法汇总
a)快排：时间复杂度O(nlogn)
思路：前两步是partition过程，第三步是递归过程
->1: 选定第一个元素作为pivot, 遍历[l+1,r]的元素，将数组分为<v和>v的部分
->2: 交换l与j+1的元素，将v放在应该在的位置，返回此时v的索引。
->3: 对<v和>v的部分递归调用快排函数
partition作用是找到把数组分成大于pivot和小于pivot的分界值的索引，partition的思想可以用来
在O（n）时间内找第k大的数，找中位数（第n/2的数），最小（大）的k个数
b)归并排序：时间复杂度O(nlogn)
思路：将数组二分，将左，右排好序的数组在合并起来。递归左右和merge两步。
二分时间复杂度O(logn)，merge时间复杂度O(n),空间复杂度O(n),以空间换时间
->1:对二分后两部分进行递归，merge_sort(lis,l,mid),merge(lis, mid+1, r)
->2:对lis从l到r遍历
->3:辅助数列tmp=lis，辅助指针i,j和k。i,j指向辅助数组的l和mid+1, k指向原数组的l
->4:比较tmp[i],tmp[j]的大小，对于升序排列，较小的值赋给lis[k]；越界情况（i>mid,j>r），直接将未越界的值赋给lis[k]
@State: PYTHON35 PASS
'''
import sys
import random
############  快排 ###########################
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
############  归并排序 ###########################
def merge_sort(lis):
    if not isinstance(lis, list):
        print("input is not list type!")        
        sys.exit(1)
    if not lis:
        return 
    merge_sort_core(lis,0,len(lis)-1)

def merge_sort_core(lis, l, r):
    if l >= r:
        return
    mid = l + (r - l) // 2
    merge_sort_core(lis, l, mid)
    merge_sort_core(lis, mid+1,r)
    merge(lis, l, mid, r)

def merge(lis, l, mid, r):
    tmp = lis
    i, j = l, mid + 1
    # for k in range(len(lis)):
    for k in range(l, r+1):
        if i > mid:
            lis[k] = tmp[j]
            j += 1
        elif j > r:
            lis[k] = tmp[i]
            i += 1
        elif tmp[i] > tmp[j]:
            lis[k] = tmp[j]
            j += 1
        else:
            lis[k] = tmp[i]
            i += 1

if __name__ == "__main__":
    lis = [random.randint(0,10) for _ in range(10)]
    lis1 = lis
    print(lis)
    quick_sort(lis)
    merge_sort(lis1)
    
    print("quick_sort",lis)
    print("merge_sort",lis1)