"""
Inch units and inch units are interchanged

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""

value = float(input('Please enter length:'))
unit = input('Please enter unit:')
if unit == 'in' or unit == '英寸':
    print('%f inches = %f centimeters'% (value, value * 2.54))
elif unit =='cm' or unit =='cm':
    print('%fcm = %finch'% (value, value / 2.54))
else:
    print('Please enter a valid unit')
