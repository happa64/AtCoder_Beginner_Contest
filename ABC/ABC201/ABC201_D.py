# https://atcoder.jp/contests/abc201/submissions/22622749
# D - Game in Momotetsu World
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    grid = tuple(tuple(input().rstrip()) for _ in range(H))

    teban = [[""] * W for _ in range(H)]
    teban[0][0] = "T"
    for h in range(H):
        for w in range(W):
            for dh, dw in ((0, 1), (1, 0)):
                nh, nw = h + dh, w + dw
                if nh >= H or nw >= W:
                    continue
                teban[nh][nw] = "T" if teban[h][w] == "A" else "A"

    res = [[None] * W for _ in range(H)]
    res[-1][-1] = 0
    for h in reversed(range(H)):
        for w in reversed(range(W)):
            now = res[h][w]
            for dh, dw in ((0, -1), (-1, 0)):
                nh, nw = h + dh, w + dw
                if nh < 0 or nw < 0:
                    continue
                if teban[nh][nw] == "T":
                    nxt = now + (1 if grid[h][w] == "+" else -1)
                else:
                    nxt = now + (-1 if grid[h][w] == "+" else 1)
                if res[nh][nw] is None:
                    res[nh][nw] = nxt
                else:
                    res[nh][nw] = max(res[nh][nw], nxt) if teban[nh][nw] == "T" else min(res[nh][nw], nxt)

    print("Draw" if res[0][0] == 0 else "Takahashi" if res[0][0] > 0 else "Aoki")


if __name__ == '__main__':
    solve()
