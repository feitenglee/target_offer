# 2019-08-26 PASS
# by lifeiteng@live.com
# 
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
def is_num(s):
    # return bool
    # 判断s是否是字符串，s是否是空串
    if not isinstance(s,str) or len(s) <= 0:
        return False
    lower_str = [x.lower() for x in s]
    if 'e' in lower_str:
        index_e = lower_str.index('e')
        front = lower_str[:index_e]
        behind = lower_str[index_e+1:]#切片索引可以超过索引范围
        if '.' in behind or len(behind) == 0:
            return False
        front_bool = scan_digit(front)
        behind_bool = scan_digit(behind)
        return front_bool and behind_bool
    else:
        num_bool = scan_digit(lower_str)
        return num_bool

def scan_digit(s):
    dot_num = 0
    allow_val = ['0','1','2','3','4','5','6','7','8','9','+','-','.']
    for i in range(len(s)):
        if s[i] not in allow_val:
            return False
        if s[i] == '.':
            dot_num += 1
        if s[i] in '+-' and i != 0:
            return False
    if dot_num > 1:
        return False
    return True

if __name__ == "__main__":
    s1 = '124e'#false
    s2 = '+124e'#false
    s3 = '1-24e' #false
    s4 = '12.4e-2'#true
    s5 = '12.4e-2.1'#false
    s6 = '+-12.421'#false
    print(is_num(s1))
    print(is_num(s2))
    print(is_num(s3))
    print(is_num(s4))
    print(is_num(s5))
    print(is_num(s6))