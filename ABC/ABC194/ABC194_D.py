# https://atcoder.jp/contests/abc194/submissions/20741647
# D - Journey
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    res = 0
    for i in range(1, n):
        res += 1 / i
    res *= n
    print(res)


if __name__ == '__main__':
    solve()
