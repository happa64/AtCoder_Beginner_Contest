# https://atcoder.jp/contests/joi2012yo/submissions/15056892
# C - 最高のピザ (Best Pizza)
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a, b = map(int, input().split())
    c = int(input())
    D = sorted(list(int(input()) for _ in range(n)), reverse=True)

    R = [0] + list(accumulate(D))
    res = 0
    for i, cal in enumerate(R):
        total = c + cal
        value = a + i * b
        res = max(res, total // value)
    print(res)


if __name__ == '__main__':
    resolve()
