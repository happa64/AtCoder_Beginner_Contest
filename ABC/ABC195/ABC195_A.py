# https://atcoder.jp/contests/abc195/submissions/20868809
# A - Health M Death
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    m, h = map(int, input().split())
    print("Yes" if h % m == 0 else "No")


if __name__ == '__main__':
    solve()
