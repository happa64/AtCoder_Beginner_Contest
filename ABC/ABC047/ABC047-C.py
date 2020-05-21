# https://atcoder.jp/contests/abc047/submissions/13455458
# C - 一次元リバーシ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    res = 0
    for i in range(1, n):
        if s[i - 1] != s[i]:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
