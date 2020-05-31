import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input().rstrip()
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    # dp:i文字目まで見て、「(の個数」が「)の個数」よりもj個多い文字列にする為の最小コスト
    dp = [[f_inf] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if S[i] == "(":
                # 操作を行わない：jは1増える
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
                # 括弧を逆転させる：jは1減る
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + C[i])
            else:
                # 括弧を逆転させる：jは1増える
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + C[i])
                # 操作を行わない：jは1減る
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])

            # 括弧を削除する：jはそのまま
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + D[i])

    print(dp[-1][0])


if __name__ == '__main__':
    resolve()
