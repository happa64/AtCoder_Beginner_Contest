# https://atcoder.jp/contests/abc209/submissions/24101063
# A - Counting
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b = map(int, input().split())
    res = max(0, b - a + 1)
    print(res)



if __name__ == '__main__':
    solve()
