#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 10:41:03
@LastEditTime: 2019-09-17 11:39:37
@Description: 
@State: PYTHON35 PASS
'''

# import sys

def find_seq(s):
    if not isinstance(s,str):
        return []
    if not s:
        return []
    # if len(s) > 100:
    #     return []
    res = []
    find_seq_core(s, res)
    result = sorted(list(set(res)))
    for x in result:
        print(x)
    return result

def find_seq_core(s, res):
    if s.find("?") == -1:
        res.append(s)
        return res
    seq_list = list(s)
    tmp1,tmp2 = seq_list,seq_list
    for i in range(len(seq_list)):
        if seq_list[i] == "?":
            tmp1[i] = "0"
            tmp1_str = ''.join(x for x in tmp1)
            find_seq_core(tmp1_str,res) 
            tmp2[i] = "1"
            tmp2_str = ''.join(x for x in tmp2)
            find_seq_core(tmp2_str,res) 

if __name__ == "__main__":
    s = "11100??11"
    s1 = "1110011"
    s2 = ""
    s3 = "???"
    find_seq(s)
    # print(find_seq(s))
    # print(find_seq(s1))
    # print(find_seq(s2))
    # print(find_seq(s3))

            
    