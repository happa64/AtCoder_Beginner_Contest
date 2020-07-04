# https://atcoder.jp/contests/aising2019/submissions/14930721
# C - Alternating Path
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = list(list(input()) for _ in range(H))

    res = [[0] * W for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if grid[y][x] == "#":
                visited[y][x] = True
                que = deque([[y, x]])
                cnt = 1
                tmp = []
                while que:
                    h, w = que.popleft()
                    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_h, next_w = h + dh, w + dw
                        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                            continue
                        if grid[h][w] == "#" and grid[next_h][next_w] == ".":
                            if not visited[next_h][next_w]:
                                que.append([next_h, next_w])
                                tmp.append([next_h, next_w])
                                visited[next_h][next_w] = True
                        elif grid[h][w] == "." and grid[next_h][next_w] == "#":
                            if not visited[next_h][next_w]:
                                cnt += 1
                                que.append([next_h, next_w])
                                visited[next_h][next_w] = True
                for h, w in tmp:
                    res[h][w] = cnt
    ans = 0
    for h in range(H):
        ans += sum(res[h])
    print(ans)


if __name__ == '__main__':
    resolve()
