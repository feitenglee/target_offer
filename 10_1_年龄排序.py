# 2019-08-27
# by lifieteng@live.com
# 对有大量重复数字的数组排序，构造辅助内存，用空间换时间
import random
import sys
import numpy as np


def sort_ages(age_min,age_max,nums):
    ages = []

    for i in range(nums):
        ages.append(random.randint(age_min,age_max))
    times_of_ages = list(np.zeros(age_max+1,dtype=int))# 缺省时float类型，需要int类型时，dtype=int
    print(ages)
    
    for age in ages:
        times_of_ages[age] += 1
    print(times_of_ages)
    index = 0
    for i in range(age_min,age_max+1):
        for j in range(times_of_ages[i]):
            ages[index] = i
            index += 1
    return ages
if __name__ == "__main__":
    # age_min,age_max,nums = sys.argv[1],sys.argv[2], sys.argv[3]# 注意命令行传进来的是str类型

    # 命令行传参1：一个一个赋值，
    # args = sys.argv[1:]
    # age_min = int(args[0])
    # age_max = int(args[1])
    # nums = int(args[2])

    # 命令行传参2：列表表达式，将字符数组转换成数字数组
    args = [int(x) for x in sys.argv[1:]]
    age_min,age_max,nums = args[0], args[1], args[2]
    ages = sort_ages(age_min,age_max,nums)
    print(ages)