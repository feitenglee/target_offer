#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 16:59:13
@LastEditTime: 2019-09-05 20:39:25
@Description: 二分查找的几道题，在已经排序的数组上
题目1：数字在排序数组中出现的次数
思路1：遍历数组，时间复杂度O(n)
思路2：已排序的数组，可使用二分查找，确定数字第一个出现的index和最后一个出现的index，作差。
->1:二分查找继续条件l<=r
->2:第一个重复数字，中间数字与前面的数字不相同；最后一个数字，中间数字与后面的数字不相同
题目2:n个数连续排在n-1长度的数组上，查找缺失的数
思路：转换为第一个数字与下标不相同的数
->1:如果mid的数字与mid不相同，前面一个数字与下标相等，则mid即为要查找的值，如果前面一个数字与下标不相等，查找左半部分
->2:如果mid的数字与mid相同，查找右半部分
->2:
@State: PYTHON35 PASS
'''
import sys
#题目1：二分查找法，数字在排序数组中出现的次数
def get_nums_of_k(lis,k):
    if not isinstance(lis,list) or not isinstance(k, int):
        print("input is not list or int type!")
        sys.exit(1)
    if not lis:
        return 0
    nums = 0
    index1 = first_k(lis, k)
    index2 = last_k(lis, k)
    # print(index1,index2)
    if index1 != -1 or index2 != -1:
        nums = index2 - index1 + 1
    return nums

def first_k(lis, k):
    l,r = 0,len(lis)-1
    while l <= r:
        mid = l + (r - l) // 2
        if k == lis[mid]:
            if (mid > 0 and lis[mid-1] != k) or mid == 0:
                return mid
            else:
                r = mid - 1
        elif k < lis[mid]:
            r = mid - 1
        else:
            l = mid + 1
    #若k不存在，返回-1
    return -1

def last_k(lis, k):
    l,r = 0,len(lis)-1
    while l <= r:
        mid = l + (r - l) // 2
        if k == lis[mid]:
            if (mid < len(lis)-1 and lis[mid+1] != k) or mid == len(lis)-1:
                return mid
            else:
                l = mid + 1
        elif k < lis[mid]:
            r = mid - 1
        else:
            l = mid + 1
    #若k不存在，返回-1
    return -1

#题目1：二分查找法，0~n-1中缺失的数字
def get_missing_num(lis):
    if not isinstance(lis, list):
        print("input is not list type")
        sys.exit(1)
    if not lis:
        print("input is empty lsit")
        sys.exit(1)
    l,r = 0,len(lis)-1
    while l <= r:
        mid = l + (r - l) // 2
        if lis[mid] == mid:
            l = mid + 1
        else:
            if mid > 0 and lis[mid-1] != mid -1:
                r = mid -1
            else:
                return mid
    
if __name__ == "__main__":
    lis = [1,2,3,3,3,3,4,5]
    lis1 = [0,1,3,4]
    lis2 = [0,1,2,4]
    lis3 = [1,2,3,4]
    print(get_nums_of_k(lis,3))
    print(get_missing_num(lis1))
    print(get_missing_num(lis2))
    print(get_missing_num(lis3))