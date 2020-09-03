# https://atcoder.jp/contests/nikkei2019-2-qual/submissions/16479159
# D - Shortest Path on a Line
import sys
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra_heap(v, start, edge):
    """
    ダイクストラ法
    :param v: 走査するグラフの頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    res = [f_inf] * v
    res[start] = 0
    checked = [False] * v
    checked[start] = True
    edge_list = []
    for u in edge[start]:
        heappush(edge_list, u)
    while len(edge_list):
        min_edge = heappop(edge_list)
        cost, node = min_edge
        if not checked[node]:
            res[node] = cost
            checked[node] = True
            for next_cost, next_node in edge[node]:
                if not checked[next_node]:
                    heappush(edge_list, [next_cost + cost, next_node])
    return res


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        """
        [left, right)のsegfuncしたものを得る
        left: index(0-index)
        right: index(0-index)
        """
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def resolve():
    n, m = map(int, input().split())
    LRC = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: [x[0], x[1]])
    dist = [f_inf] * n
    dist[0] = 0
    seg = SegTree(dist, lambda x, y: min(x, y), f_inf)
    for l, r, c in LRC:
        l -= 1
        r -= 1
        mi = seg.query(l, r)
        if dist[r] > mi + c:
            seg.update(r, mi + c)
            dist[r] = mi + c
    res = dist[-1]
    print(res if res != f_inf else -1)


def resolve2():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        l, r, c = map(int, input().split())
        edge[l - 1].append([c, r - 1])
        edge[r - 1].append([c, l - 1])
    for i in reversed(range(1, n)):
        edge[i].append([0, i - 1])

    dist = dijkstra_heap(n, 0, edge)
    print(-1 if dist[-1] == f_inf else dist[-1])


if __name__ == '__main__':
    resolve2()
