#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-30 16:05:58
@LastEditTime: 2019-08-30 16:17:06
@Description: 把最小元素放在辅助列表中，当作辅助栈
@State: PYTHON35 PASS
'''

class StackWithMin():
    def __init__(self):
        self.m_data = []
        self.m_min = []

    def push(self,data):
        self.m_data.append(data)

        if len(self.m_min) == 0 or data < self.m_min[-1]:
            self.m_min.append(data)
        else:
            self.m_min.append(self.m_min[-1])
    
    def pop(self):
        if len(self.m_data) or len(self.m_min):
            self.m_data.pop()
            self.m_min.pop()
        else:
            return
    def min(self):
        if len(self.m_data) or len(self.m_min):
            print(self.m_min[-1])
            return self.m_min[-1]
        else:
            return

if __name__=='__main__':
    a = StackWithMin()
    a.push(3)
    a.min()
    a.push(2)
    a.push(4)
    a.min()
    a.pop()
    a.min()
    a.pop()
    a.min()