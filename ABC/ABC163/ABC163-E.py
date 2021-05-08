# https://atcoder.jp/contests/abc163/submissions/22446514
# E - Active Infants
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def debug():
    from itertools import permutations
    n = int(input())
    A = tuple(map(int, input().split()))
    max_score = 0
    L = None
    for pattern in permutations(range(n)):
        score = sum(A[x] * abs(x - pattern.index(x)) for x in range(n))
        if score > max_score:
            max_score = score
            L = pattern
    print(max_score, L, [A[x] for x in L])


def solve():
    n = int(input())
    A = tuple(map(int, input().split()))
    B = [[A[i], i] for i in range(n)]
    B.sort(reverse=True)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        a, x = B[i]
        for l in range(i + 1):
            now = dp[i][l]
            if l + 1 <= n:
                dp[i + 1][l + 1] = max(dp[i + 1][l + 1], now + a * abs(x - l))
            r = n - (i - l) - 1
            if r >= 0:
                dp[i + 1][l] = max(dp[i + 1][l], now + a * abs(x - r))
    print(max(dp[-1]))


if __name__ == '__main__':
    solve()
