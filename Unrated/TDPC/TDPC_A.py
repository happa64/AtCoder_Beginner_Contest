# https://atcoder.jp/contests/tdpc/submissions/17127196
# A - コンテスト
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(map(int, input().split()))
    MAX = sum(P) + 1
    dp = [[0] * MAX for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        p = P[i - 1]
        for j in range(MAX):
            if dp[i - 1][j]:
                dp[i][j] = 1
                dp[i][j + p] = 1
    print(sum(dp[-1]))


if __name__ == '__main__':
    resolve()
