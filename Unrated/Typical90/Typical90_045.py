import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    XY = tuple(tuple(map(int, input().split())) for _ in range(n))

    # 2点間の距離を計算
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        x1, y1 = XY[i]
        for j in range(i + 1, n):
            x2, y2 = XY[j]
            dist[i][j] = dist[j][i] = pow(x1 - x2, 2) + pow(y1 - y2, 2)

    # グループ内での2点間距離の最大値を計算
    cost = [0] * (1 << n)
    for S in range(1, 1 << n):
        for i in range(n):
            for j in range(i + 1, n):
                if (S & (1 << i)) and (S & (1 << j)):
                    cost[S] = max(cost[S], dist[i][j])

    # bit dp
    dp = [f_inf] * (1 << n)
    dp[0] = 0
    for i in range(1, k + 1):
        next_dp = [f_inf] * (1 << n)
        for S in range(1, 1 << n):
            s = S
            while s:
                next_dp[S] = min(next_dp[S], max(dp[S ^ s], cost[s]))
                s = (s - 1) & S
        dp = next_dp

    print(dp[-1])


if __name__ == '__main__':
    solve()
