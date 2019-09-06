#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-03 10:37:37
@LastEditTime: 2019-09-03 14:45:13
@Description: 
思路1：构造字典，key是数字，value是次数，按照value排序
->1:空字典构造，遍历添加key, value
->2:按value逆序排序，判断第一个元素的value是否超过数组长度的一半，返回第一个元素的key
思路2：如果是已排序好的数组，判断后一位数字与当前数字是否相等，构造次数数组，索引数组
思路3：如果是已排序好的数组，数组中间的数字一定是那个出现次数超过数组长度一半的数字，即中位数(需要修改原来数组)
->1:快排 partition
->2:索引n/2
思路4：利用要找的数出现的次数比其他所有数字出现的数字还要多的特性。
->1:辅助数，一个记录result，一个记录次数“和”
->2:遍历数组，如果次数为0，更新result，次数重置为1
->3:循环内，如果后一个数与result相等，次数++;不想等，次数--
@State: PYTHON35 PASS
'''
import sys

def more_than_helf_num1(lis):
    '''
    @discription:思路一，构造字典+排序字典 
    @param {type} list 
    @return: int
    '''    
    if not isinstance(lis, list):
        print("input is not list type!")
        sys.exit(1)
    dic = {}
    for num in lis:
        # if not dic.__contains__(num):
        #     dic[num] = 1
        # if dic.__contains__(num):
        #     dic[num] += 1
        if not dic.__contains__(num):# python3中不在包含has_key,以__contains__代替
            dic[num] = 0
        dic[num] += 1
    res = sorted(dic.items(), key = lambda x:x[1],reverse=True)# 默认正序排列
    
    if 2 * res[0][1] <= len(lis) :
        print("input has no number's time larger than half of length!")
        sys.exit(1)
    return res[0][0]

def more_than_helf_num2(lis):
    '''
    @discription:思路4，时间复杂度o(n) 
    @param {type} 
    @return: 
    '''
    res = lis[0]
    times = 1
    for i in range(len(lis)-1):
        if times == 0:
            res = lis[i]
            times = 1
        if lis[i+1] != res:
            times -= 1
        if lis[i+1] == res:
            times += 1
    t = 0
    for num in lis:
        if num == res:
            t += 1
    if 2 * t <= len(lis) :
        print("input has no number's time larger than half of length!")
        sys.exit(1)
    return res
if __name__ =="__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    print(more_than_helf_num1(numbers))
    print(more_than_helf_num2(numbers))

