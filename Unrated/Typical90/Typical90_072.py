# https://atcoder.jp/contests/typical90/submissions/23740161
# 072 - Loop Railway Plan（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def dfs(cnt, sh, sw, ph, pw, h, w, H, W, visited, grid):
    res = -1
    if visited[sh][sw]:
        return cnt
    for dh, dw in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        next_h, next_w = dh + h, dw + w
        if next_h == ph and next_w == pw:
            continue
        if next_h < 0 or next_w < 0 or next_h >= H or next_w >= W or grid[next_h][next_w] == "#":
            continue
        if visited[next_h][next_w]:
            continue
        visited[next_h][next_w] = True
        res = max(res, dfs(cnt + 1, sh, sw, h, w, next_h, next_w, H, W, visited, grid))
        visited[next_h][next_w] = False
    return res


def solve():
    H, W = map(int, input().split())
    grid = tuple(input().rstrip() for _ in range(H))

    res = -1
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                continue
            res = max(res, dfs(0, h, w, -1, -1, h, w, H, W, [[False] * W for _ in range(H)], grid))
    print(res)


if __name__ == '__main__':
    solve()
