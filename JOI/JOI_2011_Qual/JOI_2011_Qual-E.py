# https://atcoder.jp/contests/joi2011yo/submissions/15049970
# E - チーズ (Cheese)
import sys
from collections import deque
import copy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, N = map(int, input().split())
    grid = [input() for _ in range(H)]
    fac = [[] for _ in range(N + 1)]
    fac_list = [str(i) for i in range(1, N + 1)]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "S":
                fac[0] = [h, w]
            elif grid[h][w] in fac_list:
                fac[int(grid[h][w])] = [h, w]

    cost_init = [[f_inf] * W for _ in range(H)]
    res = 0
    for i in range(N):
        cost = copy.deepcopy(cost_init)
        sh, sw = fac[i]
        gh, gw = fac[i + 1]
        cost[sh][sw] = 0
        que = deque([[sh, sw]])
        while que:
            h, w = que.popleft()
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_h, next_w = h + dh, w + dw
                if -1 < next_h < H and -1 < next_w < W and grid[next_h][next_w] != "X":
                    if cost[next_h][next_w] > cost[h][w] + 1:
                        cost[next_h][next_w] = cost[h][w] + 1
                        que.append([next_h, next_w])
        res += cost[gh][gw]

    print(res)


if __name__ == '__main__':
    resolve()
