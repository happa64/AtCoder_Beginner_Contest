# https://atcoder.jp/contests/nikkei2019-ex/submissions/15498260
# B - 二乗
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    for a in range(int(pow(n, 0.5)) + 1):
        if pow(a, 2) <= n:
            res = a
        else:
            break
    print(res)


if __name__ == '__main__':
    resolve()
