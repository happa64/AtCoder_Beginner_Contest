# https://atcoder.jp/contests/abc154/submissions/13479238
# A - Remaining Balls
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    print(a - 1, b) if u == s else print(a, b - 1)


if __name__ == '__main__':
    resolve()
