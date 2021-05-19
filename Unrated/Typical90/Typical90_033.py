# https://atcoder.jp/contests/typical90/submissions/22347515
# 033 - Not Too Bright（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    if H == 1:
        print(W)
    elif W == 1:
        print(H)
    else:
        print(((H + 1) // 2) * ((W + 1) // 2))


if __name__ == '__main__':
    solve()
