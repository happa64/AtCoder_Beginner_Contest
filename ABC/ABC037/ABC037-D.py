import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(h, w):
        if dp[h][w] == 0:
            num = 1
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_h, next_w = h + dh, w + dw
                if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                    continue
                elif A[next_h][next_w] <= A[h][w]:
                    continue
                else:
                    num = (num + dfs(next_h, next_w)) % mod
            dp[h][w] = num
        return dp[h][w]

    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    res = 0
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            res = (res + dfs(i, j)) % mod
    print(res)


if __name__ == '__main__':
    resolve()
