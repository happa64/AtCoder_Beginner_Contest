# https://atcoder.jp/contests/practice2/submissions/17683771
# G - SCC
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class SCC:
    """
    有向グラフを強連結成分分解する．
    dfsを2回行う実装であり，計算量はO(N+M)
    -----
    self.n : グラフの頂点数
    self.postorder : postorderの小さい順に並んだ頂点番号のリスト
    self.group : 頂点番号iの強連結成分番号
    self.reverse_graph : 元のグラフと辺の向きが逆のグラフ
    -----
    reduction() により生成
    self.red_graph : 強連結成分を縮約したグラフ
    self.red_comps : i番目の強連結成分に含まれる頂点集合
    -----
    topological_sort() により生成
    self.tp_order : 強連結成分を縮約したグラフ上の頂点番号をトポロジカル順に並べた集合
    """

    def __init__(self, graph):
        self.n = len(graph)
        self.graph = graph
        self.postorder = []
        self.group = [-1] * self.n
        self.label = 0

        # 逆辺を張ったグラフの構築
        self.reverse_graph = [[] for _ in range(self.n)]
        for u in range(self.n):
            for v in self.graph[u]:
                self.reverse_graph[v].append(u)

        # self.graph上のpostorderの計算
        self._used = [0] * self.n
        for v in range(self.n):
            if not self._used[v]:
                self._dfs(v)

        # postorderの大きい頂点から逆向きにdfs
        # 未訪問かつrev_graph上でたどり着ける頂点は同じ強連結成分に属する
        self._rused = [0] * self.n
        for v in self.postorder[::-1]:
            if not self._rused[v]:
                self._rdfs(v, self.label)
                self.label += 1

    def _dfs(self, v):
        self._used[v] = 1
        for nv in self.graph[v]:
            if not self._used[nv]:
                self._dfs(nv)
        self.postorder.append(v)

    def _rdfs(self, v, label):
        self._rused[v] = 1
        self.group[v] = label
        for nv in self.reverse_graph[v]:
            if not self._rused[nv]:
                self._rdfs(nv, label)

    def reduction(self):
        """
        強連結成分を縮約したグラフを構築
        """
        self.red_graph = [[] for _ in range(self.label)]
        self.red_comps = [[] for _ in range(self.label)]
        for v in range(self.n):
            for nv in self.graph[v]:
                if self.group[v] == self.group[nv]:
                    continue
                self.red_graph[self.group[v]].append(self.group[nv])
            self.red_comps[self.group[v]].append(v)

    def topological_sort(self):
        """
        縮約したグラフ上でトポロジカルソート
        """
        from collections import deque
        red_n = self.label

        deg = [0] * red_n  # 入次数
        for v in range(red_n):
            for nv in self.red_graph[v]:
                deg[nv] += 1

        que = deque()
        self.tp_order = []
        for i in range(red_n):
            if deg[i] == 0:
                que.append(i)
                self.tp_order.append(i)

        while que:
            u = que.popleft()
            for v in self.red_graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    que.append(v)
                    self.tp_order.append(v)


def resolve():
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)

    scc = SCC(G)
    scc.reduction()
    scc.topological_sort()

    print(scc.label)
    for i in scc.tp_order:
        print(len(scc.red_comps[i]), *scc.red_comps[i])


if __name__ == '__main__':
    resolve()
