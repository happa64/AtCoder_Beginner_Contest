# https://atcoder.jp/contests/agc017/submissions/16405221
# B - Moderate Differences
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b, c, d = map(int, input().split())
    diff = b - a
    for k in range(n):
        mi = k * c - (n - 1 - k) * d
        ma = k * d - (n - 1 - k) * c
        if mi <= diff <= ma:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
