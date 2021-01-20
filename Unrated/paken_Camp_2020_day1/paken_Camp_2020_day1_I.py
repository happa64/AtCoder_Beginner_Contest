# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19533896
# I - くねくね
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    h, w = map(int, input().split())
    sx, sy, gx, gy = map(lambda x: int(x) - 1, input().split())
    grid = tuple(input().rstrip() for _ in range(h))

    dp = [[[f_inf] * w for _ in range(h)] for _ in range(2)]
    dp[0][sx][sy] = 0
    dp[1][sx][sy] = 0
    que0 = deque([(sx, sy)])
    que1 = deque([(sx, sy)])
    while que0 or que1:
        if que0:
            x, y = que0.popleft()
            for dx, dy in [(1, 0), (-1, 0)]:
                next_x, next_y = x + dx, y + dy
                if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w or grid[next_x][next_y] == "#":
                    continue
                if dp[1][x][y] != f_inf and dp[0][next_x][next_y] > dp[1][x][y] + 1:
                    dp[0][next_x][next_y] = dp[1][x][y] + 1
                    que1.append((next_x, next_y))
        if que1:
            x, y = que1.popleft()
            for dx, dy in [(0, 1), (0, -1)]:
                next_x, next_y = x + dx, y + dy
                if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w or grid[next_x][next_y] == "#":
                    continue
                if dp[0][x][y] != f_inf and dp[1][next_x][next_y] > dp[0][x][y] + 1:
                    dp[1][next_x][next_y] = dp[0][x][y] + 1
                    que0.append((next_x, next_y))
    res = min(dp[0][gx][gy], dp[1][gx][gy])
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
