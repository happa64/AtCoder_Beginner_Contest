# https://atcoder.jp/contests/typical90/submissions/22165990
# 020 - Log Inequality（★3）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b, c = map(int, input().split())
    if a < pow(c, b):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    solve()