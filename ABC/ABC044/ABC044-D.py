# https://atcoder.jp/contests/abc044/submissions/15487773
# C - 高橋君とカード
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a = map(int, input().split())
    X = list(map(int, input().split()))
    MAX = n * a
    dp = [[[0] * (MAX + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        x = X[i - 1]
        for k in range(n):
            for s in range(MAX):
                dp[i][k][s] += dp[i - 1][k][s]
                if s + x <= MAX:
                    dp[i][k + 1][s + x] += dp[i - 1][k][s]
    res = 0
    for k in range(1, n + 1):
        res += dp[-1][k][a * k]
    print(res)


if __name__ == '__main__':
    resolve()
