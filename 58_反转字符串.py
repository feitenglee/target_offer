#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-06 10:23:15
@LastEditTime: 2019-09-06 10:59:53
@Description: 
题目1：反转单词顺序
思路1：python的split将字符串以空格分隔，转换成list，再反转list
思路2：先将整个字符串反转，再反转每个单词，将单词顺序反转正确
题目2：左旋转字符串
思路1: python中直接使用切片操作
思路2：先反转前n个字符，再反转后面的字符，最后反转整个字符串
@State: PYTHON35 PASS
'''
import sys

def reverse_word_sequence(str1):
    if not isinstance(str1, str):
        print("input is not str type!")
        sys.exit(1)
    s = str1.split(' ')
    return ' '.join(s[::-1])
    
def reverse_left_sequence(str1,n):
    if not str1:
        return ''
    return str1[n:] + str1[:n]
    
if __name__ == "__main__":
    s1 = "I am a student."
    s2 = "abcdefg"
    print(reverse_word_sequence(s1))
    print(reverse_left_sequence(s2,2))