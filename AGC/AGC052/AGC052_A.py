# https://atcoder.jp/contests/agc052/submissions/21000103
# A - Long Common Subsequence
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = tuple(input().rstrip() for _ in range(3))
    res = "0" * n + "1" * n + "0"
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
