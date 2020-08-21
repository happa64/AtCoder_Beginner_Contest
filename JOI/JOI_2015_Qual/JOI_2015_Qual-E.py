# https://atcoder.jp/contests/joi2015yo/submissions/16069131
# E - 砂の城 (Sandcastle)
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    memo = [[0] * W for _ in range(H)]
    used = [[False] * W for _ in range(H)]
    que1 = deque([])
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "." or grid[h][w] == "9":
                continue
            cnt = 0
            for dh, dw in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                next_y, next_x = h + dh, w + dw
                if grid[next_y][next_x] == ".":
                    cnt += 1
            memo[h][w] = cnt
            if cnt >= int(grid[h][w]):
                que1.append([h, w])
                used[h][w] = True

    res = 0
    while que1:
        que2 = deque([])
        while que1:
            y, x = que1.popleft()
            for dy, dx in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                next_y, next_x = y + dy, x + dx
                if grid[next_y][next_x] == "." or grid[next_y][next_x] == "9":
                    continue
                memo[next_y][next_x] += 1
                if not used[next_y][next_x] and memo[next_y][next_x] >= int(grid[next_y][next_x]):
                    que2.append([next_y, next_x])
                    used[next_y][next_x] = True
        que1 = que2
        res += 1
    print(res)


if __name__ == '__main__':
    resolve()
