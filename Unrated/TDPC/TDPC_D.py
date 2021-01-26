# https://atcoder.jp/contests/tdpc/submissions/19700500
# D - サイコロ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d = map(int, input().split())

    x = d
    cnt2 = cnt3 = cnt5 = 0
    while x % 2 == 0:
        x //= 2
        cnt2 += 1
    while x % 3 == 0:
        x //= 3
        cnt3 += 1
    while x % 5 == 0:
        x //= 5
        cnt5 += 1
    if x != 1:
        print(0)
        exit()

    dp = [[[[0] * (cnt5 + 1) for _ in range(cnt3 + 1)] for _ in range(cnt2 + 1)] for _ in range(n + 1)]
    dp[0][0][0][0] = 1
    for i in range(n):
        for j in range(cnt2 + 1):
            for k in range(cnt3 + 1):
                for l in range(cnt5 + 1):
                    now = dp[i][j][k][l]
                    dp[i + 1][j][k][l] += now * 1 / 6  # 1が出る
                    dp[i + 1][min(j + 1, cnt2)][k][l] += now * 1 / 6  # 2が出る
                    dp[i + 1][j][min(k + 1, cnt3)][l] += now * 1 / 6  # 3が出る
                    dp[i + 1][min(j + 2, cnt2)][k][l] += now * 1 / 6  # 4が出る
                    dp[i + 1][j][k][min(l + 1, cnt5)] += now * 1 / 6  # 5が出る
                    dp[i + 1][min(j + 1, cnt2)][min(k + 1, cnt3)][l] += now * 1 / 6  # 6が出る
    res = dp[n][cnt2][cnt3][cnt5]
    print(res)


if __name__ == '__main__':
    resolve()
