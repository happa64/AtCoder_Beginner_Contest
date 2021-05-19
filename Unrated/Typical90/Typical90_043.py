# https://atcoder.jp/contests/typical90/submissions/22712287
# 043 - Maze Challenge with Lack of Sleep（★4）
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    rs, cs = map(lambda z: int(z) - 1, input().split())
    rt, ct, = map(lambda z: int(z) - 1, input().split())
    S = tuple(input().rstrip() for _ in range(H))

    dp = [[[f_inf] * W for _ in range(H)] for _ in range(2)]
    dp[0][rs][cs] = dp[1][rs][cs] = 0
    que = deque([(-1, rs, cs)])
    while que:
        p, h, w = que.popleft()
        for dh, dw in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_w < 0 or next_h >= H or next_w >= W or S[next_h][next_w] == "#":
                continue
            u = 0 if dh == 0 else 1
            x = 0 if p == -1 or p == u else 1
            cost = dp[p][h][w] + x
            if dp[u][next_h][next_w] > cost:
                dp[u][next_h][next_w] = cost
                que.append((u, next_h, next_w))
    print(min(dp[0][rt][ct], dp[1][rt][ct]))


if __name__ == '__main__':
    solve()
