# https://atcoder.jp/contests/abc184/submissions/18368599
# D - increment of coins
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, C = map(int, input().split())

    dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
    dp[A][B][C] = 1
    for a in range(A, 100):
        for b in range(B, 100):
            for c in range(C, 100):
                tot = a + b + c
                now = dp[a][b][c]
                dp[a + 1][b][c] += now * a / tot
                dp[a][b + 1][c] += now * b / tot
                dp[a][b][c + 1] += now * c / tot

    res = 0
    for i in range(100):
        for j in range(100):
            k = i + j + 100 - (A + B + C)
            if k >= 0:
                res += k * (dp[i][j][100] + dp[i][100][j] + dp[100][i][j])
    print("{:.9f}".format(res))


if __name__ == '__main__':
    resolve()
