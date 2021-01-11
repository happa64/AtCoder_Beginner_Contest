# https://atcoder.jp/contests/abc188/submissions/19311886
# A - Three-Point Shot
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    diff = abs(x - y)
    print("Yes" if diff < 3 else "No")


if __name__ == '__main__':
    resolve()
