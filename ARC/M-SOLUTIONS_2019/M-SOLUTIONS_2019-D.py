# https://atcoder.jp/contests/m-solutions2019/submissions/15273165
# D - Maximum Sum of Minimum
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    def dfs(v, p):
        global res
        c = C.pop(0)
        T[v] = c
        for u in edge[v]:
            if u == p:
                continue
            else:
                res += min(T[v], C[0])
                dfs(u, v)

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    C = list(map(int, input().split()))
    C.sort(reverse=True)

    T = [0] * n
    dfs(0, -1)
    print(res)
    print(*T)


if __name__ == '__main__':
    resolve()
