# https://atcoder.jp/contests/abc126/submissions/12248382
# C - Dice and Coin
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    res = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        p = (1 / n) * pow(1 / 2, cnt)
        res += p
    print(res)


if __name__ == '__main__':
    resolve()
