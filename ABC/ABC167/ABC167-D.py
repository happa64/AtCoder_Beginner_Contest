# https://atcoder.jp/contests/abc167/submissions/13099757
# D - Teleporter
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    tree = [[] for _ in range(n)]
    for idx, a in enumerate(A):
        tree[idx].append(a - 1)

    # 1からの距離をメモしながらテレポートし、既に訪れた場所にテレポートしたら、1と閉路の開始点、終了点の各距離を配列に入れる
    def dfs(pre, dist):
        depth[pre] = dist
        for to in tree[pre]:
            if depth[to] != f_inf:
                cycle.append([depth[to], depth[pre] + 1])
                return
            else:
                dfs(to, dist + 1)

    cycle = []
    depth = [f_inf for _ in range(n)]
    dfs(0, 0)

    cycle_start = cycle[0][0]
    cycle_end = cycle[0][1]
    # kが閉路までの距離以下であれば、1から距離kの位置を出力
    if k <= cycle_start:
        print(depth.index(k) + 1)
    else:
        # kが閉路までの距離より大きければ、1から最終的な町の距離は
        # 1から閉路までの距離 +（k - 閉路までの距離）%（閉路の長さ）である
        remainder = (k - cycle_start) % (cycle_end - cycle_start)
        res = cycle_start + remainder
        print(depth.index(res) + 1)


def resolve2():
    # ダブリング：O(NlogK)なのでpypyじゃないと通りません
    n, k = map(int, input().split())
    to = [[-1] * n for _ in range(60)]
    to[0] = list(map(lambda x: int(x) - 1, input().split()))

    # 2^i回テレポートした後何処にいるのか？
    for i in range(59):
        for j in range(n):
            to[i + 1][j] = to[i][to[i][j]]

    v = 0
    for i in reversed(range(60)):
        l = 1 << i
        if l <= k:
            v = to[i][v]
            k -= l

    print(v + 1)


if __name__ == '__main__':
    resolve2()
