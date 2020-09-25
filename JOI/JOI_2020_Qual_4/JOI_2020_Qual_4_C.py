# https://atcoder.jp/contests/joi2020yo2/submissions/16999410
# C - 桁和 (Digit Sum)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
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

    res = {n}
    not_res = set()
    for i in range(1, n + 1):
        if i in res or i in not_res:
            continue
        tmp = set()
        while i < n:
            tmp.add(i)
            i += digit_sum(i)
            if i in res:
                res |= tmp
                break
            if i in not_res:
                not_res |= tmp
                break
        else:
            not_res |= tmp

    print(len(res))


if __name__ == '__main__':
    resolve()
