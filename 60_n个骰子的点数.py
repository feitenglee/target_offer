#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-12 09:47:48
@LastEditTime: 2019-09-12 10:19:39
@Description: 
思路1：辅助数组，构造骰子和字典，key是n个骰子的和，value是出现的次数，递归解决
递归的思路，将n个骰子之和查分长1个骰子点数+n-1个骰子之和
@State: PYTHON35 PASS
'''

max_val = 6
def print_probability(num):
    if num < 1:
        return
    prob = {}
    probability(num, prob)
    total = pow(max_val, num)
    for i in prob.items():
        print("{}:{:.3f}".format(i[0],i[1]/total))

def probability(num, prob):
    for i in range(1, max_val + 1):
        prob_core(num,i, prob)

def prob_core(cur, tsum, prob):
    if cur == 1:
        prob[tsum] = prob.get(tsum,0) + 1
    else:
        for i in range(1, max_val + 1):
            prob_core(cur - 1, tsum + i, prob)

if __name__ == "__main__":
    print_probability(3)