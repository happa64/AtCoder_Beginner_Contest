# https://atcoder.jp/contests/tenka1-2014-qualb/submissions/14384604
# B - エターナルスタティックファイナル
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()
    T = list(input() for _ in range(n))

    # dp:Sのi文字目までの部分文字列に一致するフレーズの並べ方の総数
    dp = [0] * (len(S) + 1)
    dp[0] = 1
    for i in range(1, len(S) + 1):
        for t in T:
            if i < len(t):
                continue
            else:
                SS = S[i - len(t):i]
                if SS == t:
                    dp[i] = (dp[i] + dp[i - len(t)]) % mod
    print(dp[-1])


if __name__ == '__main__':
    resolve()
