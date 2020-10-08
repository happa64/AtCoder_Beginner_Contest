# https://atcoder.jp/contests/abc146/submissions/13258826
# D - Coloring Edges on Tree
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append([b, i])

    def dfs(v, p, p_col):
        col = 1
        for u, idx in tree[v - 1]:
            if u == p:
                continue
            if col == p_col:
                col += 1
            res[idx] = col
            col += 1
            dfs(u, v, res[idx])

    res = [0 for _ in range(n - 1)]
    dfs(1, -1, -1)
    print(max(res))
    print("\n".join(map(str, res)))


if __name__ == '__main__':
    main()
