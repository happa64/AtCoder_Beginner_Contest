# https://atcoder.jp/contests/arc031/submissions/14454892
# B - 埋め立て
import sys
from copy import deepcopy
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    island_init = list(list(input()) for _ in range(10))

    cnt = 0
    for h in range(10):
        for w in range(10):
            if island_init[h][w] == "o":
                cnt += 1

    for h in range(10):
        for w in range(10):
            island = deepcopy(island_init)
            island[h][w] = "o"
            que = deque()
            visited = [[False] * 10 for _ in range(10)]
            res = 0
            for i in range(10):
                for j in range(10):
                    if island[i][j] == "o":
                        que.append([i, j])
                        visited[i][j] = True
                        res += 1
                        break
                else:
                    continue
                break

            while que:
                y, x = que.popleft()
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_y, next_x = y + dy, x + dx
                    if next_x < 0 or next_x >= 10 or next_y < 0 or next_y >= 10:
                        continue
                    elif island[next_y][next_x] == "x":
                        continue
                    else:
                        if not visited[next_y][next_x]:
                            visited[next_y][next_x] = True
                            res += 1
                            que.append([next_y, next_x])

            if cnt + 1 == res:
                print("YES")
                exit()
    print("NO")


if __name__ == '__main__':
    resolve()
