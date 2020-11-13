# https://atcoder.jp/contests/agc004/submissions/18072782
# B - Colorful Slimes
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    res = f_inf
    mi = [f_inf] * n
    for i in range(n):
        for j in range(n):
            mi[j] = min(mi[j], A[j - i])
        t = i * x + sum(mi)
        res = min(res, t)
    print(res)


if __name__ == '__main__':
    resolve()
