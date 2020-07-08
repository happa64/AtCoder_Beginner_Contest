# https://atcoder.jp/contests/joi2013yo/submissions/15077099
# D - 暑い日々 (Hot days)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    d, n = map(int, input().split())
    D = [int(input()) for i in range(d)]
    ABC = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * n for _ in range(d)]
    for i in range(1, d):
        now_tmp, prev_tmp = D[i], D[i - 1]
        for j in range(n):
            now_a, now_b, now_c = ABC[j]
            if now_a <= now_tmp <= now_b:
                tmp = 0
                for k in range(n):
                    prev_a, prev_b, prev_c = ABC[k]
                    if prev_a <= prev_tmp <= prev_b:
                        tmp = max(tmp, dp[i - 1][k] + abs(now_c - prev_c))
                dp[i][j] = tmp

    print(max(dp[-1]))


if __name__ == '__main__':
    resolve()
