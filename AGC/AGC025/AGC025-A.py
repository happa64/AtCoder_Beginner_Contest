# https://atcoder.jp/contests/agc025/submissions/13212117
# A - Digits Sum
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def digit_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def resolve():
    n = int(input())

    res = f_inf
    for a in range(1, n):
        b = n - a
        cnt = digit_sum(a) + digit_sum(b)
        res = min(res, cnt)

    print(res)


if __name__ == '__main__':
    resolve()
