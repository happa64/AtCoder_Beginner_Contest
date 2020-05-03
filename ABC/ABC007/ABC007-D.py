# https://atcoder.jp/contests/abc007/tasks/abc007_4
# D - 禁止された数字
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def digit_DP(S):
    L = len(S)
    # dp[決定した桁数][未満フラグ][4または9を含むか]
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(L + 1)]
    dp[0][0][0] = 1
    # 決定した桁数
    for i in range(L):
        D = int(S[i])
        # 未満フラグ 0or1
        for j in range(2):
            # 4または9を含むか 0or1
            for k in range(2):
                # 未満フラグが立っていなければ、0~9まで試す
                # 未満フラグが立っている場合、0~Dまで試す
                for d in range(10 if j else D + 1):
                    dp[i + 1][j or d < D][k or d == 4 or d == 9] += dp[i][j][k]

    return dp[L][1][1] + dp[L][0][1]


def resolve():
    a, b = map(int, input().split())
    print(digit_DP(str(b)) - digit_DP(str(a - 1)))


if __name__ == '__main__':
    resolve()
