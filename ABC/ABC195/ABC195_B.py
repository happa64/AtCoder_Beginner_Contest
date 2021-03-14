# https://atcoder.jp/contests/abc195/submissions/20879902
# B - Many Oranges
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b, w = map(int, input().split())
    w *= 1000
    mi = (w + b - 1) // b
    ma = w // a
    if mi > ma:
        print("UNSATISFIABLE")
    else:
        print(mi, ma)


if __name__ == '__main__':
    solve()
