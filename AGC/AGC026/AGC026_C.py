# https://atcoder.jp/contests/agc026/submissions/20270739
# C - String Coloring
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = list(input().rstrip())

    a, b = defaultdict(int), defaultdict(int)
    for bit in range(1 << n):
        lr, lb = "", ""
        rr, rb = "", ""
        for mask in range(n):
            if bit & (1 << mask):
                lr += s[mask]
                rr += s[n + mask]
            else:
                lb += s[mask]
                rb += s[n + mask]
        a[(lr, lb)] += 1
        b[(rr[::-1], rb[::-1])] += 1

    res = 0
    for k, v in a.items():
        res += v * b[k]
    print(res)


if __name__ == '__main__':
    resolve()
