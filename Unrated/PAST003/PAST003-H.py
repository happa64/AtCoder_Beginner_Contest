# https://atcoder.jp/contests/past202005/submissions/13531886
# H - ハードル走
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, L = map(int, input().split())
    X = set(list(map(int, input().split())))
    T = list(map(int, input().split()))

    dp = [f_inf for _ in range(L + 1)]
    dp[0] = 0

    for j in range(1, L + 1):
        for i in range(3):
            step = 2 ** i
            p = T[2] if j in X else 0

            if i == 0:
                t = T[0]
                dp[j] = min(dp[j], dp[j - step] + t + p)
            elif i == 1:
                t = T[0] + T[1]
                if j - step >= 0:
                    dp[j] = min(dp[j], dp[j - step] + t + p)
                if j == L:
                    t = T[0] * 0.5 + T[1] * 0.5
                    dp[j] = min(dp[j], dp[j - 1] + t + p)
            else:
                t = T[0] + T[1] * 3
                if j - step >= 0:
                    dp[j] = min(dp[j], dp[j - step] + t + p)
                if j == L:
                    t = T[0] * 0.5 + T[1] * 2.5
                    dp[j] = min(dp[j], dp[j - 3] + t + p)

                    t = T[0] * 0.5 + T[1] * 1.5
                    dp[j] = min(dp[j], dp[j - 2] + t + p)

                    t = T[0] * 0.5 + T[1] * 0.5
                    dp[j] = min(dp[j], dp[j - 1] + t + p)

    print(int(dp[-1]))


if __name__ == '__main__':
    resolve()
