# https://atcoder.jp/contests/abc213/submissions/24960312
# E - Stronger Takahashi
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    S = [input().rstrip() for _ in range(H)]

    dp = [[f_inf] * W for _ in range(H)]
    que = deque([(0, 0, 0)])
    while que:
        if que:
            c, h, w = que.popleft()
            if dp[h][w] != f_inf:
                continue
            dp[h][w] = c
            for dh1, dw1 in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nh, nw = h + dh1, w + dw1
                if nh < 0 or nw < 0 or nh >= H or nw >= W:
                    continue
                if dp[nh][nw] != f_inf:
                    continue
                if S[nh][nw] == ".":
                    que.appendleft((c, nh, nw))
                else:
                    for dh2 in range(-1, 2):
                        for dw2 in range(-1, 2):
                            nh2, nw2 = nh + dh2, nw + dw2
                            if nh2 < 0 or nw2 < 0 or nh2 >= H or nw2 >= W:
                                continue
                            if dp[nh2][nw2] != f_inf:
                                continue
                            que.append((c + 1, nh2, nw2))
    res = dp[-1][-1]
    # for i in dp:
    #     print(*i)
    print(res)


if __name__ == '__main__':
    solve()
