"""
Percentage to grade grade
90 points or more, output A
80 to 89 points, output B
70 minutes to 79 minutes, output C
60 minutes to 69 minutes, output D
60 points or less, output E

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""

score = float(input('Please enter score:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('The corresponding grade is:', grade)

