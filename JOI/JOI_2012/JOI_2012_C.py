# https://atcoder.jp/contests/joi2012ho/submissions/18977446
# C - 夜店 (Night Market)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t, s = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * (t + 1)
    for i in range(n):
        a, b = AB[i]
        next_dp = [0] * (t + 1)
        for j in range(t + 1):
            next_dp[j] = max(next_dp[j], dp[j])
            if j < s < j + b or t < j + b:
                continue
            next_dp[j + b] = max(next_dp[j + b], dp[j] + a)
        dp = next_dp
    print(max(dp))


if __name__ == '__main__':
    resolve()
