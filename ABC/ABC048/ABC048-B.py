# https://atcoder.jp/contests/abc048/submissions/12215095
# B - Between a and b ...
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, x = map(int, input().split())
    print(b // x + 1 - max(0, (a - 1) // x + 1))


if __name__ == '__main__':
    resolve()
