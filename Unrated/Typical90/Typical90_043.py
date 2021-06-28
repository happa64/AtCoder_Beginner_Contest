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

    dp = [[[f_inf] * W for _ in range(H)] for _ in range(4)]
    dp[0][rs][cs] = dp[1][rs][cs] = dp[2][rs][cs] = dp[3][rs][cs] = 0
    que = deque([(-1, rs, cs)])  # (直前の向き, 今いるノードの行, 今いるノードの列)
    while que:
        p, h, w = que.popleft()
        for u, (dh, dw) in enumerate(((0, 1), (1, 0), (0, -1), (-1, 0))):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_w < 0 or next_h >= H or next_w >= W or S[next_h][next_w] == "#":
                continue
            x = 0 if p == -1 or p == u else 1  # 向きが直前から変えるならコスト+1
            cost = dp[p][h][w] + x
            if dp[u][next_h][next_w] > cost:
                dp[u][next_h][next_w] = cost
                que.appendleft((u, next_h, next_w)) if x == 0 else que.append((u, next_h, next_w))
    print(min(dp[i][rt][ct] for i in range(4)))


if __name__ == '__main__':
    solve()
