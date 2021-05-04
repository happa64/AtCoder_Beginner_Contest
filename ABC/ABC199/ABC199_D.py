import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def dfs(v, edge, paint, color=0):
    if any(paint[u] == color for u in edge[v]):
        return 0
    paint[v] = color
    res = 1
    for u in edge[v]:
        if paint[u] == -1:



def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    res = 1
    paint = [-1] * n
    for i in range(n):
        if paint[i] == -1:
            continue
        paint[i] = 0
        res *= 3 * dfs(i, edge)
    print(res)


if __name__ == '__main__':
    main()
