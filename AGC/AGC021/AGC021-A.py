# https://atcoder.jp/contests/agc021/tasks/agc021_a
# A - Digit Sum 2
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
    n = input()
    l = len(n)

    res = 0
    for i in range(l):
        if i == 0:
            res += int(n[i]) - 1
        else:
            res += 9

    res = max(res, digit_sum(int(n)))
    print(res)


if __name__ == '__main__':
    resolve()
