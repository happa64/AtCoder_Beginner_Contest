# https://atcoder.jp/contests/abc207/submissions/23756248
# A - Repression
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    ABC = list(map(int, input().split()))
    ABC.sort()
    res = ABC[-1] + ABC[-2]
    print(res)

if __name__ == '__main__':
    solve()
