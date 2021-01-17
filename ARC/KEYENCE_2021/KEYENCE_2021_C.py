import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 998244353


def resolve():
    h, w, k = map(int, input().split())
    grid = [["?"] * w for _ in range(h)]
    for _ in range(k):
        i, j, c = input().split()
        grid[int(i) - 1][int(j) - 1] = c

    INV = pow(3, MOD - 2, MOD) * 2 % MOD
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][0] = pow(3, h * w - k, MOD)
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "R":
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
            elif grid[i][j] == "D":
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            elif grid[i][j] == "X":
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            else:
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j] * INV % MOD) % MOD
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * INV % MOD) % MOD
    print(dp[h - 1][w - 1])


if __name__ == '__main__':
    resolve()
