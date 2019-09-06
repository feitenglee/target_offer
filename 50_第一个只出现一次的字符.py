#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 14:43:42
@LastEditTime: 2019-09-05 15:11:37
@Description:
思路1：两层遍历，时间复杂度O(n^2)
思路2：构造哈希表，与插入顺序有关，可使用OrderedDict有序列表 
@State: PYTHON35 PASS
'''
import sys
from collections import OrderedDict
def first_no_repeating(str1):
    if not isinstance(str1, str):
        print("input is not str type")
        sys.exit(1)
    if not str1:
        return ''
    dic = OrderedDict()
    # for ele in str1:
    #     if dic.__contains__(ele):
    #         dic[ele] += 1
    #     else:
    #         dic[ele] = 1
    for ele in str1:
        dic[ele] = dic.get(ele,0) + 1 # get取键对应的值，若键不存在返回默认值0，语法dic.get(key,default=None)
    print(dic)
    for x in dic.items():
        if x[1] == 1:
            return x[0]
    print("has no char repeat only 1 times!")

if __name__ == "__main__":
    str1 = "abaccdeff"
    str2 = "abc"
    print(first_no_repeating(str1))
    # print(first_no_repeating(str2))