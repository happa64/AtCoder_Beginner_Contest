# https://atcoder.jp/contests/indeednow-quala/submissions/21172049
# D - パズル
import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def solve():
    def calc_cost(grid):
        cost = 0
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 0:
                    continue
                th, tw = divmod(grid[h][w] - 1, W)
                cost += abs(h - th) + abs(w - tw)
        return cost

    H, W = map(int, input().split())
    init_state = tuple(tuple(map(int, input().split())) for _ in range(H))
    final_state = tuple(tuple(0 if w == W - 1 and h == H - 1 else h * W + w + 1 for w in range(W)) for h in range(H))

    sh = sw = None
    for i in range(H):
        for j in range(W):
            if init_state[i][j] == 0:
                sh, sw = i, j

    visited = dict()
    visited[init_state] = calc_cost(init_state)
    que = [(calc_cost(init_state), 0, sh, sw, init_state)]
    heapify(que)
    while que:
        cost, dist, h, w, state = heappop(que)
        if state == final_state:
            print(cost)
            break
        for dh, dw in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            nh, nw = h + dh, w + dw
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            next_state = list(list(state[i]) for i in range(H))
            next_state[h][w], next_state[nh][nw] = next_state[nh][nw], next_state[h][w]
            next_state = tuple(tuple(next_state[i]) for i in range(H))
            next_cost = dist + 1 + calc_cost(next_state)
            if visited.get(next_state, f_inf) > next_cost and next_cost <= 24:
                visited[next_state] = next_cost
                heappush(que, (next_cost, dist + 1, nh, nw, next_state))


if __name__ == '__main__':
    solve()
