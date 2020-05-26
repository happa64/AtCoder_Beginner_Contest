# https://atcoder.jp/contests/dp/submissions/13594742
# B - Frog 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    H = list(map(int, input().split()))

    dp = [f_inf for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(H[i] - H[i - j]))

    print(dp[-1])


if __name__ == '__main__':
    resolve()
