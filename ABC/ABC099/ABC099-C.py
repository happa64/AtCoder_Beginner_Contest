# https://atcoder.jp/contests/abc099/submissions/12900309
# C - Strange Bank
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    List = [1]

    for i in range(1, 7):
        List.append(pow(6, i))
        List.append(pow(9, i))

    List.sort()
    dp = [f_inf for _ in range(n + 1)]
    dp[0] = 0

    for i in range(1, n + 1):
        for L in List:
            if i - L >= 0:
                dp[i] = min(dp[i], dp[i - L] + 1)

    print(dp[n])


if __name__ == '__main__':
    resolve()
