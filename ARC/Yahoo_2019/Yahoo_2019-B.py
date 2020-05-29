# https://atcoder.jp/contests/yahoo-procon2019-qual/submissions/13677722
# B - Path
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    tree = [[] for _ in range(4)]
    for _ in range(3):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    def dfs(v, p):
        for u in tree[v]:
            if u == p:
                continue
            elif visited[u]:
                return
            else:
                visited[u] = True
                dfs(u, v)
                return

    visited = [False] * 4
    visited[0] = True
    dfs(0, -1)
    print("YES" if visited.count(True) == 4 else "NO")


if __name__ == '__main__':
    resolve()
