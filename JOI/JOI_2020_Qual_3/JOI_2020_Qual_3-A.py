# https://atcoder.jp/contests/joi2020yo1c/submissions/15341065
# A - X に最も近い値 (The Nearest Value)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, l, r = map(int, input().split())
    mi = f_inf
    for i in range(l, r + 1):
        diff = abs(x - i)
        if mi > diff:
            mi = diff
            res = i
    print(res)


if __name__ == '__main__':
    resolve()
