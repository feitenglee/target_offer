#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-27 15:48:42
@LastEditTime: 2019-08-29 15:22:36
@Description: 
# 二分查找的变种，需注意特殊情况。
# 1、有序数组仍然是旋转数组。2、出现中间数字与两边数字相等的情况，采用顺序查找。
# 3、只包含一个数字的数组
@State: PYTHON35 PASS
'''


def min_rotate_list(lis):
    left,right,mid = 0,len(lis)-1,0
    if not isinstance(lis, list) or not lis:
        return # 返回None
    if lis[0] < lis[-1]:
        return lis[0]

    while (lis[left] >= lis[right]):#注意边界条件是>=
        if right - left == 1:
            mid = right
            break
        # mid = (left + right)/2#存在风险，left+right超出int的范围
        mid = left + int((right - left)/2)
        if lis[mid] == lis[right] and lis[mid] == lis[left]:
        # if lis[mid] == lis[right] == lis[left]: 
            mid = min_in_order(lis,left,right)
            break
        if lis[mid] >= lis[left]:# 必须包含等于
            left = mid
        if lis[mid] <= lis[right]:
            right = mid
    return lis[mid]

def min_in_order(lis,left,right):
    val = lis[left]
    min_index = left
    for i in range(left,right+1):
        if lis[i] <= val:
            val = lis[i]
            min_index = i
    return min_index

if __name__ == "__main__":
    list1 = [1,2,3,4,5]
    list2 = [3,4,5,1,2]
    list3 = [1,0,1,1,1]
    list4 = [2,3,3,3,3,1]
    list5 = [5,]#特殊用例，一个元素的数组
    list6 = []#特殊用例，空数组

    
    print(min_rotate_list(list1))
    print(min_rotate_list(list2))
    print(min_rotate_list(list3))
    print(min_rotate_list(list4))
    print(min_rotate_list(list5))
    print(min_rotate_list(list6))
    





    
    
