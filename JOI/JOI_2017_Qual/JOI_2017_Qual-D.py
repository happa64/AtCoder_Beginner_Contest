# https://atcoder.jp/contests/joi2017yo/submissions/15236347
# D - ぬいぐるみの整理 (Plush Toys)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    total = [0] * m
    prep = [[0] * n for _ in range(m)]
    for i in range(n):
        t = int(input()) - 1
        total[t] += 1
        prep[t][i] = 1

    R = [[0] * (n + 1) for _ in range(m)]
    for i in range(m):
        for j in range(1, n + 1):
            R[i][j] += R[i][j - 1] + prep[i][j - 1]

    dp = [f_inf] * (1 << m)
    dp[0] = 0
    for S in range(1 << m):
        left = 0
        for j in range(m):
            if S & (1 << j):
                left += total[j]
        for v in range(m):
            if (S & (1 << v)) == 0:
                right = left + total[v]
                cnt_v = R[v][right] - R[v][left]
                diff = total[v] - cnt_v
                dp[S | (1 << v)] = min(dp[S | (1 << v)], dp[S] + diff)

    print(dp[-1])


if __name__ == '__main__':
    resolve()
