# https://atcoder.jp/contests/joi2012yo/submissions/15043296
# E - イルミネーション (Illumination)
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    visited = [[False] * W for _ in range(H)]
    target = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 0 and not visited[y][x]:
                visited[y][x] = True
                que = deque([[y, x]])
                tmp = [[y, x]]
                flg = True
                while que:
                    h, w = que.popleft()
                    if h % 2 == 0:
                        D = [(0, 1), (0, -1), (1, 0), (1, 1), (-1, 1), (-1, 0)]
                    else:
                        D = [(0, 1), (0, -1), (1, 0), (1, -1), (-1, -1), (-1, 0)]
                    for dh, dw in D:
                        next_h, next_w = h + dh, w + dw
                        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                            flg = False
                            continue
                        if grid[next_h][next_w] == 1 or visited[next_h][next_w]:
                            continue
                        visited[next_h][next_w] = True
                        tmp.append([next_h, next_w])
                        que.append([next_h, next_w])
                if flg:
                    target.extend(tmp)

    visited = [[False] * W for _ in range(H)]
    res = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                que = deque([[y, x]])
                while que:
                    cnt = 6
                    h, w = que.popleft()
                    if h % 2 == 0:
                        D = [(0, 1), (0, -1), (1, 0), (1, 1), (-1, 1), (-1, 0)]
                    else:
                        D = [(0, 1), (0, -1), (1, 0), (1, -1), (-1, -1), (-1, 0)]
                    for dh, dw in D:
                        next_h, next_w = h + dh, w + dw
                        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                            continue
                        if visited[next_h][next_w] or [next_h, next_w] in target:
                            cnt -= 1
                            continue
                        if grid[next_h][next_w] == 0:
                            continue
                        cnt -= 1
                        visited[next_h][next_w] = True
                        que.append([next_h, next_w])
                    res += cnt
    print(res)


if __name__ == '__main__':
    resolve()
