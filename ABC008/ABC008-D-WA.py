# https://atcoder.jp/contests/abc008/tasks/abc008_4
# D - 金塊ゲーム(80点解法）
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    # 装置の起動順を全て試す
    for pattern in permutations(XY):
        cnt = 0
        visited = [[False for _ in range(W)] for _ in range(H)]
        for x, y in pattern:
            # 左右を探索し、端もしくは探索済みの部分に突き当たったら終了
            for dx in [-1, 1]:
                next_x = x - 1
                next_y = y - 1
                while True:
                    next_x += dx
                    if next_x < 0 or next_x >= W or visited[next_y][next_x]:
                        break
                    else:
                        visited[next_y][next_x] = True
                        cnt += 1
            # 上下を探索し、端もしくは探索済みの部分に突き当たったら終了
            for dy in [-1, 1]:
                next_x = x - 1
                next_y = y - 1
                while True:
                    next_y += dy
                    if next_y < 0 or next_y >= H or visited[next_y][next_x]:
                        break
                    else:
                        visited[next_y][next_x] = True
                        cnt += 1

        res = max(res, cnt + n)

    print(res)


if __name__ == '__main__':
    resolve()
