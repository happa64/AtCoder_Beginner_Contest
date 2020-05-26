# https://atcoder.jp/contests/dp/submissions/13612935
# G - Longest Path
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    # 各頂点の次数
    deg = [0 for _ in range(n)]
    # グラフ
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        deg[b - 1] += 1

    # 入力辺を持たないノードの集合
    que = deque([])
    for i in range(n):
        if deg[i] == 0:
            que.append(i)

    # トポロジカルソートを行いながら、入力辺を持たないノードからの最長経路を求める
    dp = [0 for _ in range(n)]
    while que:
        v = que.popleft()
        for nv in edge[v]:
            # 入力辺を一つ消す
            deg[nv] -= 1
            if deg[nv] == 0:
                que.append(nv)
                dp[nv] = max(dp[nv], dp[v] + 1)

    print(max(dp))


if __name__ == '__main__':
    resolve()
