# https://atcoder.jp/contests/abc202/submissions/22804851
# C - Made Up
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    cnt = [0] * n
    for c in C:
        b = B[c - 1]
        cnt[b - 1] += 1

    res = 0
    for a in A:
        res += cnt[a - 1]
    print(res)


if __name__ == '__main__':
    solve()
