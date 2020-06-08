# https://atcoder.jp/contests/abc036/submissions/14108058
# D - 塗り絵
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        """
        :param v:親の番号
        :param p:vの親の番号
        """
        # 一番深い所に行き、帰りがけに計算する
        child = [u for u in tree[v] if u != p]
        for u in child:
            dfs(u, v)

        # dpf[v]:頂点vを黒とした場合の、子の塗り分け方の積の総和
        # dpg[v]：頂点vを白とした場合の、子の塗り分け方の積の総和
        prod = 1
        for u in child:
            prod = prod * dpf[u] % mod
        dpg[v] = prod

        prod = 1
        for u in child:
            prod = prod * dpg[u] % mod
        dpf[v] = (dpg[v] + prod) % mod

    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    dpf = [0] * n
    dpg = [0] * n
    dfs(0, -1)
    print(dpf[0])


if __name__ == '__main__':
    resolve()
