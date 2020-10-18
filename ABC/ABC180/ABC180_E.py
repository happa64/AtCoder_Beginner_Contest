# https://atcoder.jp/contests/abc180/submissions/17460415
# E - Traveling Salesman among Aerial Cities
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XYZ = [list(map(int, input().split())) for _ in range(n)]

    dp = [[f_inf] * n for _ in range(1 << n)]
    dp[0][0] = 0
    a, b, c = XYZ[0]
    for v in range(n):
        p, q, r = XYZ[v]
        cost = abs(p - a) + abs(q - b) + max(0, r - c)
        dp[1 << v][v] = min(dp[1 << v][v], dp[0][0] + cost)

    for S in range(1 << n):
        for u in range(n):
            if not (S & (1 << u)):
                continue
            a, b, c = XYZ[u]
            for v in range(n):
                idx = S | (1 << v)
                p, q, r = XYZ[v]
                cost = abs(p - a) + abs(q - b) + max(0, r - c)
                dp[idx][v] = min(dp[idx][v], dp[S][u] + cost)
    print(dp[-1][0])


if __name__ == '__main__':
    resolve()
