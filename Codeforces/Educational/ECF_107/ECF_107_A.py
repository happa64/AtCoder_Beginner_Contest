# https://codeforces.com/contest/1511/submission/116009439
# A - Review Site
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    _ = int(input())
    R = list(map(int, input().split()))

    res = 0
    for r in R:
        if r == 1 or r == 3:
            res += 1
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
