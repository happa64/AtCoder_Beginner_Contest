# https://atcoder.jp/contests/past201912-open/submissions/13762674
# J - 地ならし
import sys
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


# ダイクストラ法
def dijkstra_heap_2d(H, W, grid, sh, sw):
    dist = [[f_inf] * W for _ in range(H)]
    dist[sh][sw] = 0
    que = [(dist[sh][sw], sh, sw)]
    heapq.heapify(que)
    while que:
        d, h, w = heapq.heappop(que)
        if dist[h][w] < d:
            continue
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue
            elif grid[next_h][next_w] == "#":
                continue
            else:
                if dist[next_h][next_w] > grid[next_h][next_w] + dist[h][w]:
                    dist[next_h][next_w] = grid[next_h][next_w] + dist[h][w]
                    heapq.heappush(que, (dist[next_h][next_w], next_h, next_w))
    return dist


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 左下から各座標への最短距離を求める
    dist1 = dijkstra_heap_2d(H, W, A, H - 1, 0)
    # 右下から各座標への最短距離を求める
    dist2 = dijkstra_heap_2d(H, W, A, H - 1, W - 1)
    # 右上から各座標への最短距離を求める
    dist3 = dijkstra_heap_2d(H, W, A, 0, W - 1)

    res = f_inf
    # 経由する座標を決め打ちする
    for h in range(H):
        for w in range(W):
            # (決め打ちした座標から左下,右下,左上へのコストの合計)-(決め打ちした座標のコスト重複分)
            cost = dist1[h][w] + dist2[h][w] + dist3[h][w] - A[h][w] * 2
            res = min(res, cost)
    print(res)


if __name__ == '__main__':
    resolve()
