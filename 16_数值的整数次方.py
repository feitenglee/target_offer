# 2019-08-28 PASS
# by lifieteng@live.com
# 代码完整性：指数为负的情况，底为0的情况
# 0 的 0次方数学上无意义，详细的情况可以单独考虑这种情况
# 位运算提高效率

def power_define(base, exp):
    if base == 0 or exp == 0:
        return 1
    if exp < 0:
        # tmp = power_unsigned(base,abs(exp))
        tmp = power_quick(base,abs(exp))
        return 1/tmp
    # return power_unsigned(base,exp)
    return power_quick(base,exp)

def power_unsigned(base, exp):
    res = 1
    for _ in range(exp):
        res *= base
    return res

def power_quick(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    res = power_quick(base,exp>>1)#使用移位运算代替除2
    res = res * res
    if exp & 1 == 1:# 使用与运算代替求余运算判断幂数是奇数时
        res *= base
    return res
if __name__ == "__main__":
    print(power_define(2,3))
    print(power_define(2,-3))
    print(power_define(2,0))
    print(power_define(0,2))
    # print(power_define(64,64))