class SCC:
    """
    有向グラフを強連結成分分解する．
    dfsを2回行う実装であり，計算量はO(N+M)
    -----
    self.n : グラフの頂点数
    self.order : orderの小さい順に並んだ頂点番号のリスト
    self.group : 頂点番号iの強連結成分番号
    self.reverse_graph : 元のグラフと辺の向きが逆のグラフ
    -----
    reduction() により生成
    self.red_graph : 強連結成分を縮約したグラフ
    self.red_comps : i番目の強連結成分に含まれる頂点集合
    -----
    topological_sort() により生成
    self.top_order : 強連結成分を縮約したグラフ上の頂点番号をトポロジカル順に並べた集合
    """
    def __init__(self, graph):
        self.n = len(graph)
        self.graph = graph
        self.order = []
        self.group = [-1] * self.n

        self.reverse_graph = [[] for _ in range(self.n)]
        for u in range(self.n):
            for v in self.graph[u]:
                self.reverse_graph[v].append(u)

        self._used = [False] * self.n
        for v in range(self.n):
            if not self._used[v]:
                self._dfs(v)

        self.label = 0
        self._reverse_used = [False] * self.n
        for v in self.order[::-1]:
            if not self._reverse_used[v]:
                self._reverse_dfs(v, self.label)
                self.label += 1

    def _dfs(self, v):
        self._used[v] = True
        for nv in self.graph[v]:
            if not self._used[nv]:
                self._dfs(nv)
        self.order.append(v)

    def _reverse_dfs(self, v, label):
        self._reverse_used[v] = True
        self.group[v] = label
        for nv in self.reverse_graph[v]:
            if not self._reverse_used[nv]:
                self._reverse_dfs(nv, label)

    def reduction(self):
        """ 強連結成分を縮約したグラフを構築 """
        self.red_graph = [[] for _ in range(self.label)]
        # self.red_comps = [[] for _ in range(self.label)]
        for v in range(self.n):
            g = self.group[v]
            # self.red_comps[g].append(v)
            for nv in self.graph[v]:
                if self.group[nv] != g:
                    self.red_graph[g].append(self.group[nv])

    def topological_sort(self):
        """ 縮約したグラフ上でトポロジカルソート """
        from collections import deque
        ind = [0] * self.label
        for v in range(self.label):
            for nv in self.red_graph[v]:
                ind[nv] += 1
        que = deque([i for i in range(self.label) if ind[i] == 0])
        self.top_order = []
        while que:
            u = que.popleft()
            self.top_order.append(u)
            for v in self.red_graph[u]:
                ind[v] -= 1
                if ind[v] == 0:
                    que.append(v)