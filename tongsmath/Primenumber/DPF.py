#!/usr/bin/env python
# coding: utf-8
from math import *


def prime_number_list(n):
    l = list(range(n + 1))
    l.remove(0)
    l.remove(1)
    cnt = 0
    for i in range(2 + cnt, ceil(sqrt(n)) + 1):
        for j in l:
            if j != i and j % i == 0:
                l.remove(j)
    return l if l else False


def is_primenumber(n):
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def DPF(n):
    if n <= 1:
        raise ValueError(f'Can\'t find {n}\'s result.')
    l = prime_number_list(ceil(sqrt(n)))
    rst = []
    cnt = 1
    for i in l:
        f = is_primenumber(n)
        if n == 1 or (f and cnt == 1):
            break
        elif cnt > 1 and f:
            rst.append(n)
            break
        else:
            while n % i == 0:
                rst.append(i)
                n //= i
                cnt += 1
    return rst if rst else False


if __name__ == '__main__':
    a = int(eval((input("Enter a number:"))))
    print(a, ":", DPF(a))
