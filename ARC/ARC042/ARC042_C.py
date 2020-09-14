# https://atcoder.jp/contests/arc042/submissions/16745035
# C - おやつ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, p = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    AB.sort(reverse=True)

    res = 0
    dp = [0] * (p + 1)
    for i in range(1, n + 1):
        next_dp = [0] * (p + 1)
        a, b = AB[i - 1]
        for j in range(p + 1):
            if j + a <= p:
                next_dp[j + a] = max(next_dp[j + a], dp[j] + b)
            next_dp[j] = max(next_dp[j], dp[j])

        for k in range(i + 1, n + 1):
            _, b = AB[k - 1]
            res = max(res, next_dp[-1] + b)
        dp = next_dp
    print(res)


if __name__ == '__main__':
    resolve()
