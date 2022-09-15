from random import random

num = int(input())
for x in range(1,num+1):
    c_c_num = str(random())
    if c_c_num.startswith('4') or c_c_num.startswith('5') or c_c_num.startswith('6'):
        if len(c_c_num) == 16:
            for n in c_c_num:
                if n == '-':
                    continue
                else:
                    n = int(n)
                    if 0<=n<=9:
                        



