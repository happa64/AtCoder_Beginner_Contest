# https://atcoder.jp/contests/abc212/submissions/24645024
# A - Alloy
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b = map(int, input().split())
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Alloy")


if __name__ == '__main__':
    solve()
