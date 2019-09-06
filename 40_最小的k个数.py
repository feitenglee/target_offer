#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-03 14:46:07
@LastEditTime: 2019-09-03 15:11:22
@Description: 
思路1：排序数组，返回前k个数，时间复杂度O(nlogn)
思路2：构造容量为k个容器,遍历数组存放比容器中最大数字小的数
->1:辅助数，一个长度k的数组，一个存放数组最大数的数
->2:遍历数组，如果新数比最大数大，替换最大数
@State: PYTHON35 PASS
'''
import sys
def find_min_k_nums(lis, k):
    if not isinstance(lis, list) or not isinstance(k, int):
        print("inputs are not list or int type!")
        sys.exit(1)
    if k == len(lis):
        return lis
    if k > len(lis) or k <= 0:
        print("k must be positive and not larger than length of lis!")
        sys.exit(1)
    if not lis:
        return []
    container = lis[:k]
    for i in range(k,len(lis)):
        max_val = max(container)
        max_index = container.index(max_val)
        if lis[i] < max_val:
            container.pop(max_index)
            container.append(lis[i])
    return container


if __name__ == "__main__":
    lis = [4,5,1,6,2,7,3,8]
    lis2 = []

    print(find_min_k_nums(lis,4))
    print(find_min_k_nums(lis,8))
    print(find_min_k_nums(lis,9))
    print(find_min_k_nums(lis2,2))