# https://codeforces.com/contest/1487/submission/115861735
# C - Minimum Ties
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())

    m = (n - 1) // 2
    outcome = [[0] * n for _ in range(n)]
    j = 1
    for i in range(n):
        k = 0
        nj = j
        while k < m:
            outcome[i][nj] = 1
            outcome[nj][i] = -1
            nj = (nj + 1) % n
            k += 1
        j = (j + 1) % n

    res = []
    for i in range(n):
        for j in range(i + 1, n):
            res.append(outcome[i][j])
    print(*res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
