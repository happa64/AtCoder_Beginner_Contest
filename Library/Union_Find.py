# Union Find（経路圧縮有）
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 親が同じか判別
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 根を繋ぎ直す
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 親が同じか判別
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 連結成分の大きさを返す
    def size(self, x):
        return -self.parents[self.find(x)]


def kruskal(max_node, edge):
    """
    :param max_node: UnionFind木に渡す頂点数です
    :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
    :return: 最小全域木のコストの和
    """
    edge.sort()
    uf = UnionFind(max_node)
    cost_sum = 0
    for cost, node1, node2 in edge:
        if not uf.same(node1, node2):
            cost_sum += cost
            uf.union(node1, node2)
    return cost_sum
