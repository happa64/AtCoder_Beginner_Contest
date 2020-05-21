# https://atcoder.jp/contests/arc064/submissions/13458364
# E - Cosmic Rays
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        バリアからバリアに移動する際の最短距離は、座標の中心から座標の中心に移動した時の距離である。
        つまり、バリア間の距離を重みとした、各座標の最短距離を計算すれば良い。
        これはダイクストラ法にて求めることができる。

    計算量：O(n^2)
    """
    xs, ys, xt, yt = map(int, input().split())
    n = int(input())
    # 始点と終点も含めて、座標とバリアー径の配列を作る
    XYR = [[xs, ys, 0], [xt, yt, 0]]
    for _ in range(n):
        x, y, r = map(int, input().split())
        XYR.append([x, y, r])

    # 各座標間の移動コストを計算する
    cost = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        x1, y1, r1 = XYR[i]
        for j in range(n + 2):
            x2, y2, r2 = XYR[j]
            dist = max(0, pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5) - (r1 + r2))
            cost[i][j] = cost[j][i] = dist

    # ダイクストラ法
    def dijkstra(s):
        # 始点sから各頂点への最短距離
        # n:頂点数, cost[u][v]:辺uvのコスト(存在しないときはinf)
        d = [f_inf] * (n + 2)
        used = [False] * (n + 2)
        d[s] = 0

        while True:
            v = -1
            # まだ使われてない頂点の中から最小の距離のものを探す
            for k in range(n + 2):
                if (not used[k]) and (v == -1):
                    v = k
                elif (not used[k]) and d[k] < d[v]:
                    v = k
            if v == -1:
                break
            used[v] = True

            for m in range(n + 2):
                d[m] = min(d[m], d[v] + cost[v][m])
        return d

    res = dijkstra(0)
    print(res[1])


if __name__ == '__main__':
    resolve()
