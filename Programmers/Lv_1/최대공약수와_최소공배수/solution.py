import math


def solution(n, m):
    a = n
    b = m
    while 1:
        if a == b:
            return [math.gcd(n, m), a]
        elif a < b:
            a += n
        elif a > b:
            b += m