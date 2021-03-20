# https://atcoder.jp/contests/abc196/submissions/21096245
# D - Hanjo
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def dfs(y, x, cnt):
        res = 0
        if cnt == a:
            return 1

        for h in range(H):
            if h < y:
                continue
            for w in range(W):
                if h == y and w < x:
                    continue
                if visited[h][w]:
                    continue
                visited[h][w] = True
                if h + 1 < H and not visited[h + 1][w]:
                    visited[h + 1][w] = True
                    res += dfs(h, w, cnt + 1)
                    visited[h + 1][w] = False
                if w + 1 < W and not visited[h][w + 1]:
                    visited[h][w + 1] = True
                    res += dfs(h, w, cnt + 1)
                    visited[h][w + 1] = False
                visited[h][w] = False
        return res

    H, W, a, b = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    print(dfs(0, 0, 0))


if __name__ == '__main__':
    solve()
