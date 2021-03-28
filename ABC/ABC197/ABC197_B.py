# https://atcoder.jp/contests/abc197/submissions/21299070
# B - Visibility
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W, x, y = map(int, input().split())
    grid = tuple(input() for _ in range(H))
    x -= 1
    y -= 1
    cnt = 1
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        step = 1
        while True:
            nx, ny = x + dx * step, y + dy * step
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                break
            if grid[nx][ny] == "#":
                break
            cnt += 1
            step += 1
    print(cnt)


if __name__ == '__main__':
    solve()
