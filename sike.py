#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-23 19:33:22
@LastEditTime: 2019-09-23 20:21:23
@Description: 
@State: PYTHON35 PASS
'''
def t(a = []):
    a.append(1)
    print(a)
def test1():
    a = '1232....flow_cts_source_group_tag'
    b = a.replace('..','.').replace('..','.').replace('.','\':\'')
    c = b.split('\n')
    for line in c:
        line = '\'' + line + '\','
        print(line)

def main():
    
if __name__ == "__main__":
    # t()
    # t()
    # t()
    # t()
    test1()