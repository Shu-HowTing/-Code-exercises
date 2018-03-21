# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
递归求数值的整数次方
'''
def Power(base, exponent):
    abs_exponent = abs(exponent)
    if abs_exponent == 0:
        return 1
    if abs_exponent == 1:
        return base
    result = Power(base, abs_exponent>>1)
    result *= result
    if abs_exponent & 0x01 == 1:
        result *= base
    return result if  exponent > 0 else 1/result
print(Power(5,4))
print(Power(5,-3))


