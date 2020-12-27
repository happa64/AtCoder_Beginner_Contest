# https://atcoder.jp/contests/joi2016ho/submissions/19012878
# A - オレンジの出荷 (Oranges)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, k = map(int, input().split())
    A = list(int(input()) for _ in range(n))

    dp = [f_inf] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        ma = 0
        mi = f_inf
        for j in range(1, m + 1):
            if i - j >= 0:
                ma = max(ma, A[i - j])
                mi = min(mi, A[i - j])
                cost = k + j * (ma - mi)
                dp[i] = min(dp[i], dp[i - j] + cost)
    print(dp[-1])


if __name__ == '__main__':
    resolve()
